def initUI(self):
    link = "https://aif.ru/culture/person/maykl_dzhekson_stal_samoy_vysokooplachivaemoy_mertvoy_znamenitostyu_forbes"
    text = "Майкл Джексон стал самой высокооплачиваемой мертвой знаменитостью"
    self.label = QLabel(f'<a href={link} style="text-decoration:none; color:red;">{text}</a>', self)
    self.label.setOpenExternalLinks(True)
    self.label.show()
