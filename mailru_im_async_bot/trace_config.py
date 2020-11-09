from asyncio import CancelledError
from mailru_im_async_bot import log
import datetime
import aiohttp


def is_printable_content_type(content_type):
    return 'text' in content_type or 'json' in content_type or 'xml' in content_type or 'html' in content_type


async def on_request_start(session, trace_config_ctx, params):
    trace_config_ctx.time_start = datetime.datetime.now()
    trace_config_ctx.method = params.method
    trace_config_ctx.url = params.url
    trace_config_ctx.headers = "\n".join((f"{key}: {value}" for (key, value) in params.headers.items()))
    trace_config_ctx.chunk = None


async def on_request_chunk_sent(session, trace_config_ctx, params):
    trace_config_ctx.chunk = params.chunk[:1000]


async def on_request_end(session, trace_config_ctx, params):
    trace_config_ctx.time_end = datetime.datetime.now()
    # if params.response.content_type in ('application/json', 'text/html', None):
    if is_printable_content_type(params.response.content_type):
        params.response._text = await params.response.text()
    else:
        params.response._text = "[binary data]"

    log.debug(
        "\n[request {time}]\n{method} {url}\n{headers}\n{body}".format(
            time=trace_config_ctx.time_start,
            method=trace_config_ctx.method,
            url=trace_config_ctx.url,
            headers=trace_config_ctx.headers,
            body=str(trace_config_ctx.chunk) + "\n" if trace_config_ctx.chunk else ""
        ))

    log.debug(
        "\n[response {time}]\n{status_code} {reason}\n{headers}\n{body}\n".format(
            time=trace_config_ctx.time_end,
            status_code=params.response.status,
            reason=params.response.reason,
            headers="\n".join((f"{key}: {value}" for (key, value) in params.response.headers.items())),
            body=params.response._text
        )
    )


async def on_request_exception(session, trace_config_ctx, params):
    trace_config_ctx.time_end = datetime.datetime.now()
    if isinstance(params.exception, CancelledError):
        log.debug(
            "\n[request {time}]\n{method} {url}\n{headers}{body}".format(
                time=trace_config_ctx.time_start,
                method=trace_config_ctx.method,
                url=trace_config_ctx.url,
                headers=trace_config_ctx.headers,
                body=str(trace_config_ctx.chunk) + "\n" if trace_config_ctx.chunk else ""
            ))
        log.warning("request cancelled")
    else:
        log.exception("\n[request {time}]\n{method} {url}\n{headers}\n{type_}{exception}\n".format(
            time=trace_config_ctx.time_start,
            method=trace_config_ctx.method,
            url=trace_config_ctx.url,
            headers=trace_config_ctx.headers,
            type_=str(type(params.exception)),
            exception=str(params.exception)
        ))


trace_config = aiohttp.TraceConfig()
trace_config.on_request_start.append(on_request_start)
trace_config.on_request_end.append(on_request_end)
trace_config.on_request_chunk_sent.append(on_request_chunk_sent)
trace_config.on_request_exception.append(on_request_exception)