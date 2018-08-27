 if((statement.find("калькулятор")!=-1) or (statement.find("calculator")!=-1)):
                        self.osrun('calc')
                               
                    if((statement.find("блокнот")!=-1) or (statement.find("notepad")!=-1)):
                        self.osrun('notepad')
                        
                    #if((statement.find("skyrim")!=-1)):
                        #self.openurl('"C:\Games\Skyrim Legendary Edition\GameLauncher.exe"', "Приятной игры")
                        
                    if((statement.find("dota")!=-1) or (statement.find("доту")!=-1)):
                        self.openurl('steam://rungameid/570', "Приятной игры")
                             
                    if((statement.find("paint")!=-1) or (statement.find("паинт")!=-1)):
                        self.osrun('mspaint')

                    if((statement.find("browser")!=-1) or (statement.find("браузер")!=-1)):
                        self.openurl('http://google.ru', 'Открываю браузер')
 
                    # Команды для открытия URL в браузере
 
                    if(((statement.find("новости")!=-1) or (statement.find("новость")!=-1) or (statement.find("на усть")!=-1))):
                        self.openurl('https://ua.news/ua/', 'Открываю новости')
                         
                    if((statement.find("mail")!=-1) or (statement.find("майл")!=-1) or (statement.find("открой почту")!=-1)):
                        self.openurl('https://mail.google.com/mail/', 'Открываю почту')
                        
                    if((statement.find("вконтакте")!=-1) or (statement.find("vk")!=-1) or (statement.find("в контакте")!=-1)):
                        self.openurl('http://vk.com', 'Открываю Вк')
                    
                    if((statement.find("facebook")!=-1) or (statement.find("fb")!=-1)):
                        self.openurl('www.facebook.com', 'Открываю facebook')

                    # Команды для поиска в сети интернет

                  
                    if((statement.find("найти")!=-1) or (statement.find("поиск")!=-1) or (statement.find("найди")!=-1) or (statement.find("дайте")!=-1) or (statement.find("mighty")!=-1)):
                        statement=statement.replace('найди', '')
                        statement=statement.replace('найти', '')
                        statement=statement.strip()
                        self.openurl('https://www.google.com/search?q=' + statement, "Я нашла следующие результаты")
                        
                    if((statement.find("смотреть")!=-1) and ((statement.find("фильм")!=-1) or (statement.find("film")!=-1))):
                        statement=statement.replace('посмотреть', '')
                        statement=statement.replace('смотреть', '')
                        statement=statement.replace('хочу', '')
                        statement=statement.replace('фильм', '')
                        statement=statement.replace('film', '')
                        statement=statement.strip()
                        self.openurl('http://kinogo.cc/' + statement, "Выберите фильм")

                    if((statement.find("youtube")!=-1) or (statement.find("ютуб")!=-1) or (statement.find("you tube")!=-1) or (statement.find("на ютубе")!=-1) or (statement.find("смотреть")!=-1)):
                        statement=statement.replace('хочу', '')
                        statement=statement.replace('на ютубе', '')
                        statement=statement.replace('на ютуб', '')
                        statement=statement.replace('на youtube', '')
                        statement=statement.replace('на you tube', '')
                        statement=statement.replace('на youtub', '')
                        statement=statement.replace('youtube', '')
                        statement=statement.replace('ютуб', '')
                        statement=statement.replace('ютубе', '')
                        statement=statement.replace('посмотреть', '')
                        statement=statement.replace('смотреть', '')
                        statement=statement.strip()
                        self.openurl('http://www.youtube.com/results?search_query=' + statement, 'Ищу в ютуб')


                    if((statement.find("слушать")!=-1) and (statement.find("песн")!=-1)):
                        statement=statement.replace('песню', '')
                        statement=statement.replace('песни', '')
                        statement=statement.replace('песня', '')
                        statement=statement.replace('песней', '')
                        statement=statement.replace('послушать', '')
                        statement=statement.replace('слушать', '')
                        statement=statement.replace('хочу', '')
                        statement=statement.strip()
                        self.openurl('https://soundcloud.com/search?q=' + statement, "Нажмите плэй")
                        self.say(str("Окрыт soundcloud"))


                    # Поддержание диалога
                    
                    if((statement.find("до свидания")!=-1) or (statement.find("досвидания")!=-1) or (statement.find("закрыть system")!=-1) or (statement.find("закрыть систему")!=-1)):
                        answer = "Отключение системы!"
                        self.say(str(answer))
                        while pygame.mixer.music.get_busy():
                            time.sleep(0.1)
                        sys.exit()
                    
                    print("Вы сказали: {}".format(statement))