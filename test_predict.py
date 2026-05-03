import app as myapp, traceback

myapp.app.config['TESTING'] = True
myapp.app.config['PROPAGATE_EXCEPTIONS'] = True
client = myapp.app.test_client()

try:
    resp = client.post('/predictdata', data={
        'gender': 'male',
        'ethnicity': 'group A',
        'parental_level_of_education': "associate's degree",
        'lunch': 'standard',
        'test_preparation_course': 'none',
        'reading_score': '70',
        'writing_score': '60'
    })
    print('STATUS:', resp.status_code)
    if resp.status_code == 200:
        html = resp.data.decode()
        if 'result-score' in html:
            print('SUCCESS - Prediction result found in page!')
        else:
            print('Page rendered OK but result box not shown')
    else:
        print(resp.data.decode()[:800])
except Exception:
    traceback.print_exc()
