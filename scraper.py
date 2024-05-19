from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_song_data(title, artist):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    url = f'https://vibe.naver.com/search?query={title} {artist}'
    driver.get(url)

    print(f"Accessing URL: {url}")  # 디버깅 로그 추가

    songs = []
    song_elements = driver.find_elements(By.CSS_SELECTOR, 'div.title a')[:5]  # 적절한 CSS 선택자로 변경

    for song_element in song_elements:
        try:
            song_title = song_element.text
            song_artist = song_element.find_element(By.XPATH, '../../div[contains(@class, "artist")]/a').text
            song_link = song_element.get_attribute('href')
            album_img = song_element.find_element(By.XPATH, '../../../img').get_attribute('src')

            print(f"Title: {song_title}, Artist: {song_artist}, Link: {song_link}, Image: {album_img}")  # 디버깅 로그 추가

            songs.append({
                'title': song_title,
                'artist': song_artist,
                'link': song_link,
                'album_img': album_img
            })
        except Exception as e:
            print(f"Error scraping song element: {e}")  # 디버깅 로그 추가

    driver.quit()
    return {'songs': songs}
