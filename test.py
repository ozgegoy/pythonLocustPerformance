from locust import HttpUser, task, between


class HomePageUser(HttpUser):
    host = "https://kariyer.baykartech.com/en"

    wait_time = between(1, 3)

    @task
    def load_home_page(self):
        response = self.client.get("")
        if response.status_code == 200:
            print("Ana sayfa başarıyla yüklendi.")
        else:
            print(f"Ana sayfa yüklenemedi! HTTP Durum Kodu: {response.status_code}")

    @task
    def load_login_page(self):
        response = self.client.get("/hesaplar/login/?next=/en/dashboard/")
        if response.status_code == 200:
            print("Login sayfa başarıyla yüklendi.")
        else:
            print(f"Login sayfa yüklenemedi! HTTP Durum Kodu: {response.status_code}")

    @task
    def login(self):
        payload = {
            "login": "",
            "password": "",
        }

        url = "/hesaplar/login/?next=/en/dashboard/"

        with self.client.post(url, data=payload, headers={"Content-Type": "application/x-www-form-urlencoded"},
                              allow_redirects=False) as response:
            if response.status_code == 200:
                print("Giriş başarılı!")
            else:
                print(f"Giriş başarısız! HTTP Durum Kodu: {response.status_code}")


    @task
    def load_pages(self):
        pages = ["/yuksek-irtifa", "/open-positions/?type=1", "/internship/", "/sss", "https://baykartech.com/en/", ]
        for page in pages:
            response = self.client.get(page)
            if response.status_code == 200:
                print(f"{page} başarıyla yüklendi.")
            else:
                print(f"{page} yüklenemedi! HTTP Durum Kodu: {response.status_code}")