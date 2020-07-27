from firebase import firebase

firebase = firebase.FirebaseApplication('https://helloworldfromron.firebaseio.com')

result = firebase.get('/User',None)
print(result)

data = {'Age':27 ,'Home':'Punjab'}

# post = firebase.post('/User/Name',data)

# put = firebase.put('/User','LastName','RMEHTA')

# delete = firebase.delete('/User','LastName')

print(firebase.get('/Office','NewOfficeName'))