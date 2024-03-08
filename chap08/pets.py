def describe_pet(pet_name, animal_type = 'dog'):
    """반려동물 정보를 표시합니다"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'harry') #위치 인수
# describe_pet(pet_name='harry', animal_type='hamster') #키워드 인수

# 개
describe_pet('willie')
describe_pet(pet_name = 'willie')

# 햄스터
describe_pet('harry','hamster') 
describe_pet(pet_name='harry', animal_type='hamster') 
