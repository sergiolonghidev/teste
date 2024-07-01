import requests
import sys

def fetch_universities():
    base_url = "https://jsonmock.hackerrank.com/api/universities"
    all_universities = []
    page = 1

    while True:
        response = requests.get(f"{base_url}?page={page}")
        data = response.json()
        all_universities.extend(data['data'])
        
        if page >= data['total_pages']:
            break
        page += 1

    return {
        "page": 1,
        "per_page": len(all_universities),
        "total": len(all_universities),
        "total_pages": 1,
        "data": all_universities
    }

def highestInternationalStudents(data, city1, city2):
    city1_universities = [uni for uni in data['data'] if uni['location']['city'].lower() == city1.lower()]
    city2_universities = [uni for uni in data['data'] if uni['location']['city'].lower() == city2.lower()]

    for uni in city1_universities + city2_universities:
        uni['international_students'] = int(uni['international_students'].replace(',', ''))

    if city1_universities:
        return max(city1_universities, key=lambda x: x['international_students'])['university']
    elif city2_universities:
        return max(city2_universities, key=lambda x: x['international_students'])['university']
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <CityName1> <CityName2>")
        sys.exit(1)

    city1, city2 = sys.argv[1], sys.argv[2]
    universities_data = fetch_universities()
    result = highestInternationalStudents(universities_data, city1, city2)
    print(result if result else "No university found in the given cities.")