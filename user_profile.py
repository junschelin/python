# def build_profile(first, last, **user_info):
#     """사용자에 대해 아는 정보를 전부 딕셔너리에 저장합니다"""
#     user_info['first_name'] = first #first_name : key / first : value
#     user_info['last_name'] = last #last_name : key / last : value
#     return user_info

# user_profile = build_profile('albert', 'einstein', location='princeton', field = 'physics')

# print(user_profile)

def build_profile(first, last, **user_info):
    """사용자에 대해 아는 정보를 전부 딕셔너리에 저장합니다"""
    user_info['first_name'] = first #first_name : key / first : value
    user_info['last_name'] = last #last_name : key / last : value
    return user_info

user_profile = build_profile('juns_chelin', 'Lee', univ_='PNU', major = 'M.E')

print(user_profile)


def send_my_money(name, **user_information):
    user_information['name'] = name
    return user_information

transfer_info = send_my_money('COSTCO', howmuch='100$', bank='Hana')

print(transfer_info)

def sing_a_song(singer, **song_information):
    song_information['singer'] = singer
    return song_information

song_info = sing_a_song('Brown_eyed_soul', name='정말 사랑했을까', released_year='??')

print(song_info)