from botcity.core import DesktopBot
import pyautogui


def RetificaçãoImu(contador, cont, bot: DesktopBot, self: DesktopBot, executation=None):
 
   while (contador < cont):    
               
                     self.wait(1000)
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_keys(["ctrl", "c"])
                     bot.type_keys(["ctrl", "tab"])     
                     
                     imagen = ["pesquisar", "pesquisar2"]

                     for image in imagen:
                        try:
                           if not bot.find( image, matching=0.90, waiting_time=3000):  # Reduzi o waiting_time para 5000 ms
                             self.not_found(image)
                           bot.click()
                           break  # Se encontrou a imagem, sai do loop
                        except:
                            continue
                     

                     bot.type_keys(["ctrl", "v"])
                     bot.type_keys(["enter"])
                     self.wait(2000)

                     bot.type_down()

                     self.wait(4000)
                     bot.type_up()

              
                     imagens = ["dados" ]

                     for imagem in imagens:
                        try:
                           if not bot.find(imagem, matching=0.90, waiting_time=3000):  # Reduzi o waiting_time para 5000 ms
                             self.not_found(imagem)
                           bot.click()
                           break  # Se encontrou a imagem, sai do loop
                        except:
                           bot.type_keys(["ctrl", "tab"])
                           bot.type_down()    
                           bot.type_keys(["ctrl", "tab"])              
                           RetificaçãoImu(contador, cont, bot=self, self=self)  

                     
                     self.wait(1000)
                     if not bot.find( "interessado", matching=0.97, waiting_time=10000):
                           self.not_found("interessado")
                     bot.click_relative(94, 65)

                     self.wait(1000)
                     if not bot.find( "interessado", matching=0.97, waiting_time=10000):
                           self.not_found("interessado")
                     bot.double_click_relative(94, 65)
                     
                     try:
                        if not bot.find( "maximizar", matching=0.97, waiting_time=10000):
                           self.not_found("maximizar")
                        bot.click()
                     except:  
                        bot.type_keys(["ctrl", "tab"])
                        bot.type_down()
                        bot.type_keys(["ctrl", "tab"])
                        RetificaçãoImu(contador, cont, bot=self, self=self)

   
                     imagenss = ["nomedadossei1" , "nomedadossei2" ]

                     for imagemm in imagenss:
                        try:
                           if not bot.find(imagemm, matching=0.90, waiting_time=3000):  # Reduzi o waiting_time para 5000 ms
                             self.not_found(imagemm)
                           bot.triple_click_relative(46, 46)
                           break  # Se encontrou a imagem, sai do loop
                        except:
                           continue  # Continua tentando a próxima imagem
                     
                     bot.type_keys(["ctrl", "c"])
                     bot.type_down()
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_left()
                     bot.type_left()
                     bot.type_keys(["ctrl", "v"])
                     bot.type_keys(["ctrl", "tab"]) 
                     bot.type_down()
                     bot.type_down()
                     bot.type_down()

                     try:  
                        if not bot.find( "cidade2", matching=0.97, waiting_time=10000):
                           self.not_found("cidade2")
                        bot.click()
                     except:
                        if not bot.find( "fechar2", matching=0.97, waiting_time=10000):
                           self.not_found("fechar2")
                        bot.click()
                        self.wait(1000)    
                        bot.type_keys(["ctrl", "tab"])
                        bot.type_right()
                        bot.type_right()   
                        bot.type_down()    
                        bot.type_keys(["ctrl", "tab"])              
                        RetificaçãoImu(contador, cont, bot=self, self=self)    


                     imagensss = [ "CNPJRET" , "ccpf" ]

                     for imagemmm in imagensss:
                        try:
                           if not bot.find(imagemmm, matching=0.90, waiting_time=3000):  # Reduzi o waiting_time para 5000 ms
                             self.not_found(imagemmm)
                           bot.triple_click_relative(65, 39)
                           break  # Se encontrou a imagem, sai do loop
                        except:
                           continue  # Continua tentando a próxima imagem

                  
                     bot.type_keys(["ctrl", "c"])
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_right()
                     bot.type_keys(["ctrl", "v"])
                     bot.type_keys(["ctrl", "tab"])                            
                                 
                     bot.right_click()

                     if not bot.find( "pesquisargoo", matching=0.97, waiting_time=10000):
                         self.not_found("pesquisargoo")
                     bot.click()                    
                     self.wait(1000)    

                     pyautogui.move(-30,10)
                        
                     if not bot.find( "cidade22", matching=0.97, waiting_time=10000):
                         self.not_found("cidade22")
                     bot.click_relative(25, 39)
                        
                     bot.type_keys(["ctrl", "c"])
                        
                        #pyautogui.click(r'.\resources\cidade22.png')
                        #pyautogui.move(-30,10)
                        #pyautogui.drag(250,40,0.25)       

                   
                     if not bot.find( "fechartradutor", matching=0.97, waiting_time=10000):
                         self.not_found("fechartradutor")
                     bot.click()

                     self.wait(2000)

                     bot.click()
                     
                     
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_right()
                     bot.type_right()
                     bot.type_keys(["ctrl", "v"])
                     bot.type_left()
                     bot.type_down()
                     bot.type_keys(["ctrl", "tab"])

                     contador   = contador + 1
        











































































































































































































































































































































































































































































































































































































































































