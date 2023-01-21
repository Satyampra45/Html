class Mobile:
    fp = "sex"
    @classmethod
    def sho_model(cls,r):
        cls.ram=r
        print("realme x", cls.fp)
        print("ram:",cls.ram)
realme = Mobile()
Mobile.sho_model('8GB')      #calling class method
