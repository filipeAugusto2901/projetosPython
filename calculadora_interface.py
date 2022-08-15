
def Calculate(event): 
    
    button = event.widget.cget("text") 
  
    
    global key_matrix, inp, ans_to_print 
  
    try: 
      if button == u"\u221A": 
            ans = float(inp.get())**(0.5) 
            ans_to_print = str(ans) 
            inp.set(str(ans)) 
elif button == "c":  
            inp.set("") 
elif button == "!":  
            def fact(n): return 1 if n == 0 else n*fact(n-1) 
            inp.set(str(fact(int(inp.get())))) 
elif button == "<-":  
            inp.set(inp.get()[:len(inp.get())-1]) 
elif button == "=":  
              ans_to_print = str(eval(inp.get())) 
            inp.set(ans_to_print) 
else: 
              inp.set(inp.get()+str(button)) 
  
    except: 
      inp.set("Wrong Operation") 
  
for i in range(len(key_matrix)):   
    
    for j in range(len(key_matrix[i])):   
        btn_dict["btn_"+str(key_matrix[i][j])] = Button( 
          root, bd=1, text=str(key_matrix[i][j]), font=myFont) 
        
        btn_dict["btn_"+str(key_matrix[i][j])].grid( 
          row=i+1, column=j, padx=5, pady=5, ipadx=5, ipady=5) 
        
        btn_dict["btn_"+str(key_matrix[i][j])].bind('<Button-1>', Calculate) 
root.mainloop() 