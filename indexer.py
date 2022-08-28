
def get_path()->str:
    print("Relative path to file : ")
    path = input()
    return path

def get_file_data(path:str)->tuple(str,list[str]):
    file = open(path,"r")
    copy_content=file.read()
    lines = file.readlines()
    file.close()
    return copy_content,lines

def create_index(lines:list[str])->list[str]:
    index=[]
    new_content=[]
    for line in lines:
        if "#" in line:
            index.append(line)
  
    new_content.append("INDEX")
    new_content.append("\n\n")
    new_content+=index
    new_content.append("\n\n")
    new_content+=lines
    return new_content
    
def reformat_file_with_index(path:str,new_content:list):

    file = open(path,"w")
    file.write("")
    file.close()
    file = open(path,"w")
    file.writelines(new_content)
    file.close()


def create_copy(path:str,content:str):
    #create copy just in case
    file = open(path+"_copy","w")
    file.write(content)
    file.close()


def main():

    path=get_path()
    copy_content,lines=get_file_data(path)
    create_copy(path,copy_content)
    new_content=create_index(lines)
    reformat_file_with_index(path,new_content)


if __name__ =="__main__":
    main()
