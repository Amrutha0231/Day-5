import hashlib

url_mapping = {}

def shorten_url(long_url):
    md5_hash = hashlib.md5(long_url.encode()).hexdigest()
    short_url = "http://short.ly/" + md5_hash[:6] 
    return short_url

def main():
    while True:
        long_url = input("Enter a long URL: ")
        if long_url in url_mapping:
            short_url = url_mapping[long_url]
            print(f"Shortened URL: {short_url}")
        else:
            short_url = shorten_url(long_url)
            url_mapping[long_url] = short_url
            print(f"Shortened URL: {short_url}")

if __name__ == "__main__":
    main()
