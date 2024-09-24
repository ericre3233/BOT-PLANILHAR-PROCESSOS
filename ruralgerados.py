from botcity.core import DesktopBot


def ruralgerados(contador, cont, bot: DesktopBot, self: DesktopBot, executation=None):

    while (contador < cont):
                       
                     self.wait(1000)
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_keys(["ctrl", "c"])
                     bot.type_keys(["ctrl", "tab"])
                     
                   
                     if not bot.find( "pesq", matching=0.85, waiting_time=1000):
                         self.not_found("pesq")
                     bot.click()
                     
                     bot.type_keys(["ctrl", "v"])
                     bot.type_keys(["enter"])
                     self.wait(1000)
                     bot.type_down()
                     #self.wait(1000)  



                     imagens = ["nomegerados1" , "nomegerados2" , "razao" , "razao2"]

                     for imagem in imagens:
                        try:
                           if not bot.find( imagem, matching=0.85, waiting_time=1000):  # Reduzi o waiting_time para 5000 ms
                             self.not_found(imagem)
                           bot.triple_click_relative(82, 63)
                           break  # Se encontrou a imagem, sai do loop
                        except:
                            from RestituiçãoRural import RestituiçãoRural
                            RestituiçãoRural(contador, cont, bot=self, self=self)
                            


                     bot.type_keys(["ctrl", "c"])
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_keys(["left"] * 2) 
                     bot.type_keys(["f2", "ctrl", "v"])
                     bot.type_keys(["backspace"] * 2) 
                     bot.type_keys(["tab"])
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_keys(["pageDown"])
                     
                     
                     imagenss = ["cpfgerados1", "cpfgerados2", "cnpjgerados1", "cnpjgerados2"]

                     for imagemm in imagenss:
                        try:
                           if not bot.find( imagemm, matching=0.85, waiting_time=1000):  # Reduzi o waiting_time para 5000 ms
                             self.not_found(imagemm)
                           bot.triple_click_relative(45, 59)
                           break  # Se encontrou a imagem, sai do loop
                        except:
                           continue  # Continua tentando a próxima imagem
                        
                        

                     bot.type_keys(["ctrl", "c"])
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_keys(["f2", "ctrl", "v"])
                     bot.type_keys(["backspace"] * 2) 
                     bot.type_keys(["tab", "tab" ])
                     bot.type_keys(["ctrl", "tab"])

                    

                    # Lista com as imagens a serem procuradas
                     imagensss = ["municipio", "municipio2", "municipio3" ]

                     for imagemmm in imagensss:
                        try:
                           if not bot.find( imagemmm, matching=0.85, waiting_time=1000):  # Reduzi o waiting_time para 5000 ms
                             self.not_found(imagemmm)
                           bot.triple_click_relative(66, 59)
                           break  # Se encontrou a imagem, sai do loop
                        except:
                           continue  # Continua tentando a próxima imagem



                     bot.type_keys(["ctrl", "c"])
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_keys(["f2", "ctrl", "v"])
                     bot.type_keys(["backspace"] * 2) 
                     self.enter()
                     bot.type_left()
                     bot.type_keys(["ctrl", "tab"])                      
                      
                     
                     contador   = contador + 1
 
      



              
              
              
              
              



       














              






















































































































































































































































































































































































































































































































