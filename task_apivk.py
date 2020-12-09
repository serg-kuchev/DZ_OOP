import requests


with open('token.txt', 'r') as file_object:
    token = file_object.read().strip()


class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.token = token
        self.version = version
        self.params = {
            'access_token': self.token,
            'v': self.version
        }
        self.owner_id = requests.get(self.url + 'users.get', self.params).json()['response'][0]['id']

    def get_friend(self, user_id=None):
        if user_id is None:
            user_id = self.owner_id
        friends_url = self.url + 'friends.get'
        friends_params = {
            'count': 1000,
            'user_id': user_id
        }
        res = requests.get(friends_url, params={**self.params, **friends_params})
        return res.json()

    def __and__(self, user1, user2):
        c = user_1 and user_2
        return c



        # return(user1['response']['items'] & user2['response']['items'])

    # def get_id(self, user_id=None):
    #     if user_id is None:
    #         user_id = self.owner_id
    #     id_url = self.url + 'account.getProfileInfo'
    #     id_params = {
    #         'user_id': user_id
    #     }
    #     res = requests.get(id_url, params=id_params)
    #     return res.json()



vk_client = VkUser(token, '5.126')
friends_1 = vk_client.get_friend()
friends_2 = vk_client.get_friend(40242864)
print(friends_1 and friends_2)
# print(f'vk.com/id{str(vk_client.owner_id)}')


