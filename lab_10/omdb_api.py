import math
import requests

API_KEY = "29ff3b1e"  # argaghulamahmad@gmail.com ombd account

"""
    Fungsi untuk mendapatkan data json menggunakan api ombd
"""
def search_movie(judul, tahun):
    print("METHOD SEARCH MOVIE")

    # Generate url untuk mendapatkan data
    get_tahun = ""
    if not tahun == "-":
        get_tahun = "&y=" + tahun

    url = "http://www.omdbapi.com/?s=" + judul + get_tahun + "&apikey=" + API_KEY
    print(url)

    # Ambil data menggunakan url yang telah digenerate
    req = requests.get(url)
    resp = req.json()
    print(resp)

    data_exist = False
    stResponse = resp['Response']
    print("RESPONSE => ", stResponse)

    # Pagination
    pages = 0
    if stResponse == "True":
        count_results = resp['totalResults']

        # cukup ambil 30 data saja
        cp = (int(count_results) / 10)
        if cp > 3:
            pages = 3
        elif cp >= 0 and cp <= 3:
            pages = math.ceil(cp)
        data_exist = True

    print("Number of pages: " + str(pages))

    past_url = url
    all_data = []

    # Salin data ke list all_data
    if data_exist:
        print("DATA EXIST")
        for page in range(int(pages)):
            page += 1
            get_page = "&page=" + str(page)
            new_url = past_url + get_page
            print(new_url)
            new_req = requests.get(new_url).json()
            get_datas = new_req['Search']
            for data in get_datas:
                all_data.append(data)

    print("ALL DATA")
    print(all_data)
    return all_data

"""
    Fungsi untuk mendapatkan informasi mengenai detail sebuah film
"""
def get_detail_movie(id):
    url = "http://www.omdbapi.com/?i=" + id + "&apikey=" + API_KEY
    req = requests.get(url)
    rj = req.json()  # dict
    my_list = create_json_from_dict(rj)

    print("MY LIST")
    print(my_list)
    return my_list

"""
    Fungsi untuk men'generate' data json dari dict
"""
def create_json_from_dict(your_dict):
    your_data = {}
    for key in your_dict:
        cvalue = (your_dict.get(key))
        nk = str(key).lower()
        if type(cvalue) == list:
            nv = cvalue
        else:
            nv = cvalue.encode('ascii', 'ignore')
        your_data[nk] = nv
    return your_data
