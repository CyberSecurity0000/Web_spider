import scrapy

from urllib.parse import urlparse

from twisted.internet.error import (
    ConnectionRefusedError,
    TimeoutError,
    DNSLookupError,
    ConnectError,
)


class DynamicSpider(scrapy.Spider):

    name = "dynamic_spider"

    # ==========================================================
    # EXTENSÕES DE ARQUIVOS INTERESSANTES
    # ==========================================================

    interesting_extensions = (
        ".pdf",
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".txt",
        ".zip",
        ".rar",
        ".7z",
        ".tar",
        ".gz",
        ".conf",
        ".config",
        ".bak",
        ".old",
        ".backup",
        ".sql",
        ".log",
        ".env",
    )

    # ==========================================================
    # STATUS HTTP QUE QUEREMOS OBSERVAR
    # ==========================================================

    handle_httpstatus_list = [403, 404]

    # ==========================================================
    # INICIALIZAÇÃO
    # ==========================================================

    def __init__(self, target="", *args, **kwargs):

        super().__init__(*args, **kwargs)

        # ------------------------------------------------------
        # 1. VALIDA O ALVO
        # ------------------------------------------------------

        if not target:
            raise ValueError(
                "❌ Erro: forneça um domínio ou URL."
            )

        # ------------------------------------------------------
        # 2. NORMALIZA O ALVO
        # ------------------------------------------------------

        parsed = urlparse(
            target if "://" in target else f"https://{target}"
        )

        clean_target = parsed.hostname

        if not clean_target:
            raise ValueError(
                "❌ Erro: não foi possível identificar o domínio."
            )

        self.target = clean_target

        # ------------------------------------------------------
        # 3. DEFINE O ESCOPO
        # ------------------------------------------------------

        self.allowed_domains = [clean_target]

        # ------------------------------------------------------
        # 4. DEFINE OS PONTOS DE ENTRADA
        # ------------------------------------------------------

        self.start_urls = [
            f"http://{clean_target}",
            f"https://{clean_target}",
        ]

        self.logger.info(
            f"🎯 Alvo definido: {clean_target}"
        )

    # ==========================================================
    # VERIFICA SE A URL É UM ARQUIVO INTERESSANTE
    # ==========================================================

    def is_interesting_file(self, url):

        parsed = urlparse(url)

        # Analisa somente o caminho.
        # Isso evita problemas com:
        #
        # documento.pdf?download=1

        path = parsed.path.lower()

        return path.endswith(
            self.interesting_extensions
        )

    # ==========================================================
    # NORMALIZA E FILTRA LINKS
    # ==========================================================

    def normalize_link(self, response, link):

        if not link:
            return None

        link = link.strip()

        # ------------------------------------------------------
        # IGNORA ESQUEMAS DESNECESSÁRIOS
        # ------------------------------------------------------

        if link.startswith((
            "#",
            "mailto:",
            "javascript:",
            "tel:",
            "data:",
            "ftp:",
            "file:",
        )):
            return None

        # ------------------------------------------------------
        # TRANSFORMA URL RELATIVA EM ABSOLUTA
        # ------------------------------------------------------

        full_url = response.urljoin(link)

        parsed = urlparse(full_url)

        # ------------------------------------------------------
        # ACEITA SOMENTE HTTP / HTTPS
        # ------------------------------------------------------

        if parsed.scheme not in ("http", "https"):
            return None

        return full_url

    # ==========================================================
    # PROCESSA A PÁGINA
    # ==========================================================

    def parse(self, response):

        self.logger.info(
            f"🌐 [{response.status}] {response.url}"
        )

        # ------------------------------------------------------
        # 1. REGISTRA STATUS HTTP INTERESSANTES
        # ------------------------------------------------------

        if response.status == 403:

            self.logger.warning(
                f"🚫 403 Forbidden: {response.url}"
            )

        elif response.status == 404:

            self.logger.warning(
                f"❌ 404 Not Found: {response.url}"
            )

        # ------------------------------------------------------
        # 2. NÃO TENTA CRAWLEAR RESPOSTAS DE ERRO
        # ------------------------------------------------------

        if response.status >= 400:
            yield {
                "type": "http_error",
                "status": response.status,
                "url": response.url,
            }

            return

        # ------------------------------------------------------
        # 3. EXTRAI TODOS OS LINKS
        # ------------------------------------------------------

        links = response.css(
            "a::attr(href)"
        ).getall()

        for link in links:

            full_url = self.normalize_link(
                response,
                link
            )

            if not full_url:
                continue

            # --------------------------------------------------
            # 4. IDENTIFICA ARQUIVOS INTERESSANTES
            # --------------------------------------------------

            if self.is_interesting_file(full_url):

                self.logger.info(
                    f"📂 Arquivo encontrado: {full_url}"
                )

                yield {
                    "type": "interesting_file",
                    "url": full_url,
                    "source": response.url,
                }

                # Não trata o arquivo como página HTML
                continue

            # --------------------------------------------------
            # 5. CONTINUA O CRAWLING
            # --------------------------------------------------

            yield response.follow(
                full_url,
                callback=self.parse,
                errback=self.errback,
            )

    # ==========================================================
    # TRATAMENTO DE ERROS DE CONEXÃO
    # ==========================================================

    def errback(self, failure):

        request = failure.request
        url = request.url

        # ------------------------------------------------------
        # CONNECTION REFUSED
        # ------------------------------------------------------

        if failure.check(ConnectionRefusedError):

            error_type = "connection_refused"

            self.logger.warning(
                f"🔴 Connection refused: {url}"
            )

        # ------------------------------------------------------
        # TIMEOUT
        # ------------------------------------------------------

        elif failure.check(TimeoutError):

            error_type = "timeout"

            self.logger.warning(
                f"⏱️ Timeout: {url}"
            )

        # ------------------------------------------------------
        # DNS
        # ------------------------------------------------------

        elif failure.check(DNSLookupError):

            error_type = "dns_error"

            self.logger.warning(
                f"🌐 DNS error: {url}"
            )

        # ------------------------------------------------------
        # OUTROS ERROS DE CONEXÃO
        # ------------------------------------------------------

        elif failure.check(ConnectError):

            error_type = "connect_error"

            self.logger.warning(
                f"🔌 Connection error: {url}"
            )

        # ------------------------------------------------------
        # ERRO DESCONHECIDO
        # ------------------------------------------------------

        else:

            error_type = "unknown_error"

            self.logger.warning(
                f"⚠️ Erro ao acessar: {url}"
            )

            self.logger.warning(
                f"Detalhes: {failure.value}"
            )

        # ------------------------------------------------------
        # RETORNA O ERRO COMO ITEM
        # ------------------------------------------------------

        yield {
            "type": "request_error",
            "error": error_type,
            "url": url,
        }
