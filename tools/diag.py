import urllib.request,json
B="29f98e10-a489-4c82-ae5e-489dbcd4912f"
for u in [f"https://storage.googleapis.com/storage/v1/b/{B}/o?prefix=it&maxResults=50",f"https://storage.googleapis.com/{B}/it_apt.geojson",f"https://storage.googleapis.com/{B}/it_asp.geojson"]:
    try:
        r=urllib.request.urlopen(u,timeout=60);b=r.read();print("OK",u,len(b),b[:600])
    except Exception as e:
        print("ERR",u,e, getattr(e,'read',lambda:b'')()[:300])
