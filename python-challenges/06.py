def retrieve_zip_file():
    import urllib
    filename = "channel.zip"
    url = "http://www.pythonchallenge.com/pc/def/channel.zip"
    urllib.urlretrieve(url=url, filename=filename)
    return filename


def navigate_in_files():
    from zipfile import ZipFile
    import re

    files = ZipFile(retrieve_zip_file(), 'r')

    history = ["90052.txt"]
    pattern = re.compile("[0-9]{2,5}")

    while True:
        response = files.read("".join(history[-1]))
        number = "".join(pattern.findall(response))
        if number == "":
            break
        history.append("{fileinfo}.txt".format(fileinfo=number))
        print response

    return history, files


def show_message():
    history, files = navigate_in_files()
    print "".join([files.getinfo(name).comment for name in history])

if __name__ == "__main__":
    show_message()

# next url: http://www.pythonchallenge.com/pc/def/hockey.html
# next url: http://www.pythonchallenge.com/pc/def/oxygen.html
