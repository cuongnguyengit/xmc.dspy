# first line: 104
@NotebookCacheMemory.cache(ignore=['arg'])
def send_hftgi_request_v01_wrapped(arg, url, ports, **kwargs):
    return send_hftgi_request_v01(arg, url, ports, **kwargs)
