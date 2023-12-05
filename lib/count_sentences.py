#!/usr/bin/env python3

class MyString:
  
  def __init__(self,value=""):
    self.value=value
  
  def get_value(self):
    return self._value

  def set_value(self,value):
    if type(value)==str:
      self._value=value
    else:
      print("The value must be a string.")

  value=property(get_value,set_value)

  def is_sentence(self):
    return self.value.endswith(".")

  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
    
    new_value=self.value.replace("!",".")
    new_value=new_value.replace("?",".")

    count_list=[x for x in new_value.split(".") if x != ""]
    print(count_list)
    return len(count_list)
  
test = MyString("This lab. Will Definetly be! Annoying to do?")
print(test.is_question())
print(test.count_sentences())




