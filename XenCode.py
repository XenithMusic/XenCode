import pygame,time,colorsys,math,tkinter; from tkinter import filedialog

leftcontrol = 0
leftshift = 0
leftalt = 0
rightcontrol = 0
rightshift = 0
rightalt = 0

def openfile():
    global text
    filename = filedialog.askopenfilename()
    root.destroy()
    f = open(filename, 'r')
    data = f.readlines()
    print("DATA: " + '\n'.join(data))
    print(data)
    data = '\n'.join(data)
    data = data.split('\n\n')
    data = '\n'.join(data)
    data = data.split('\n')
    text = data
    openname = filename
    #del filename,data
    return(data)

def save():
    global openname
    print(openname)
    if openname == False:
        print("determined saveas")
        a = saveas()
        f = open(a,"w")
        f.write('\n'.join(text))
        f.close()
        openname = a
        del f,a
        print("saved to " + openname)
    else:
        print("determined normalsave")
        a = openname
        f = open(a,"w")
        f.write('\n'.join(text))
        f.close()
        openname = a
        del f,a
        print("saved to " + openname)

def saveas():
    global openname
    filename = filedialog.asksaveasfilename()
    root.destroy()
    openname = str(filename)
    del filename
    return openname


def getxbetween(lines):
    getx = 0
    for i in range(lines):
        getx += max(len(text[i]), 1)
    print(getx)
    return(getx)

def rgbfhsv(tuple):
    value = tuple
    value = (value[0]/255,value[1]/255,value[2]/255)
    print(colorsys.hsv_to_rgb(value[0],value[1],value[2]))
    out = colorsys.hsv_to_rgb(value[0],value[1],value[2])
    out = (out[0]*255,out[1]*255,out[2]*255)
    return out

def ascii(code):
    global cursorx,cursory,oldcursorx
    getmods = pygame.key.get_mods()
    print("mods: " + str(getmods))
    if code <= 127 and code not in [0,8,13,27,127,48,49,50,51,52,53,54,55,56,57,111,115]:
        if getmods & pygame.KMOD_SHIFT:
            return(str(chr(code)).upper())
        return(str(chr(code)))
    else:
        if code == 0:
            return("")
        if code == 8:
            return("Backspace")
        if code == 13:
            return(str(chr(11)))
        if code == 27:
            return("Escape")
        if code == 1073741904:
            cursorx -= 1
            if cursorx < 0:
                cursory -= 1
                cursorx = len(text[cursory])
                if cursory < 0:
                    cursory = 0
                    cursorx = 0
                    return("")
                else:
                    cursorx = len(text[cursory])
            oldcursorx = cursorx


            return("")
        if code == 1073741903:

            cursorx += 1
            if cursorx > len(text[cursory]):
                if cursory != len(text)-1:
                    cursory += 1
                    cursorx = 0
                    print(len(text))
                    print(cursory)
                    if cursory > len(text):
                        cursory = len(text)-1
                        cursorx = 0
                        return("")
                    else:
                        cursorx = 0
                else:
                    cursorx -= 1
            oldcursorx = cursorx


            return("")
        if code == 1073741906:
            if cursory != 0:
                cursory -= 1
                if cursorx >= len(text[cursory]):
                    oldcursorx = cursorx
                    cursorx = len(text[cursory])
                else:
                    cursorx = oldcursorx

        if code == 1073741905:
            if cursory != len(text)-1:
                cursory += 1
                if cursorx >= len(text[cursory]):
                    oldcursorx = cursorx
                    cursorx = len(text[cursory])
                else:
                    cursorx = oldcursorx

        if code == 111:
            if getmods & pygame.KMOD_CTRL:
                openfile()


        if code == 115:
            global a
            if getmods & pygame.KMOD_CTRL:
                if getmods & pygame.KMOD_SHIFT:
                    a = saveas()
                    f = open(a,"w")
                    f.write('\n'.join(text))
                    f.close()
                    openname = a
                    del f,a
                    print("saved to " + openname)
                    pygame.display.set_caption("XenCode - " + openname.split("/")[-1])

                else:
                    save()
            else:
                if getmods & pygame.KMOD_SHIFT:
                    return("")
                return("")
        if code == 127:
            return("Delete")

        return("")


openname = False
root = tkinter.Tk()
pygame.init()
pygame.font.init()


size = (1000,750)
charsize = (11,22)
sizewithmargin = (size[0]-(25*2),size[1]-(25*2))
charsforwrapx = round(sizewithmargin[0]/charsize[0])
charsforwrapy = round(sizewithmargin[1]/charsize[1])
print(charsforwrapx)
print(charsforwrapy)

display = pygame.display.set_mode(size)
pygame.display.set_caption("XenCode - .txt")
clock = pygame.time.Clock()
stop = False
rainbow =     (0,127,255)   # HSV
black =       (0,0,0)       # RGB
darkrainbow = (0,255,50)    # HSV
ui          = (32,32,32)  # RGB
white       = (255,255,255) # RGB
gray        = (160,160,160) # RGB
lightgray   = (224,224,224) # RGB

# CODE HIGHLIGHTING COLORS

variable    = (50,100,255)
statement   = (255,110,110)
functionnbi = (92,222,140)
functionbi  = (round(92/1.25),round(222/1.25),round(140/1.25))

# back to normal vars

display.fill(ui)
font = pygame.font.Font("./firamono.ttf",18)
adown = 0
text = [""]
combinedtext = '\n'.join(text)
cursorx    = 0
oldcursorx = 0
cursory    = 0
selecting  = 0
cursorframe= 0
cursorvis  = 0
saving     = 0
textinput  = 0
selectstart= 0
selectend  = 0
pygame.key.start_text_input()
pygame.key.set_repeat(200,60) # delay, time to repeat again
while not stop:
    try:
        tkinter.quit()
    except:
        pass
    display.fill(ui)
    combinedtext = '\n'.join(text)
    tempmousexloc = round((pygame.mouse.get_pos()[0]-25)/11)
    tempmouseyloc = math.floor((pygame.mouse.get_pos()[1]-25)/18)
    cursorframe += 1
    if cursorframe == 6:
        cursorvis = not cursorvis
        cursorframe = 0
    if tempmouseyloc in range(0,len(text)+1) and tempmouseyloc > 0:
        if tempmousexloc in range(0 ,len(text[tempmouseyloc-1])+1):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
            if selecting == 1:
                selectend = tempmousexloc+getxbetween(tempmouseyloc)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            stop = True

        if e.type == pygame.TEXTINPUT:
            allowkeydownevt = 0
            print("textinput: " + e.text)
            if "" not in e.text and chr(9) not in e.text:
                text[cursory] = text[cursory][:cursorx] + e.text + text[cursory][cursorx:]
                cursorx += 1


        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                try:
                    selecting = 1
                    selectstart = tempmousexloc+getxbetween(tempmouseyloc)
                except:
                    pass
        if e.type == pygame.MOUSEBUTTONUP:
            if e.button == 1:
                try:
                    selecting = 0
                    selectend = tempmousexloc+getxbetween(tempmouseyloc)
                except:
                    pass
                if selectstart == selectend:
                    selectstart = 0

                if e.pos[0] >= 25 and e.pos[1] >= 25:
                    mousexloc = round((e.pos[0]-25)/11)
                    mouseyloc = math.floor((e.pos[1]-25)/18)
                    try:
                        if text[mouseyloc-1][mousexloc-1]:
                            pass
                        if mouseyloc > 0:
                            print(str(mousexloc) + " " + str(mouseyloc))
                            cursorx = mousexloc
                            oldcursorx = cursorx
                            cursory = mouseyloc-1
                    except:
                        pass

        if e.type == pygame.KEYDOWN:
            if e.key in [0,8,13,27,127,111,115] or not e.key <= 127:
                print(int(e.key))
                keytext = ascii(int(e.key))
                print("keydown: " + keytext)
                if len(keytext) == 1 and keytext not in ["",chr(9)]:
                    text[cursory] = text[cursory][:cursorx] + keytext + text[cursory][cursorx:]
                    cursorx += 1

                else:
                    if keytext == "Backspace":

                        cursorx -= 1
                        if cursorx != -1:
                            text[cursory] = text[cursory][:cursorx] + text[cursory][cursorx+1:]
                        else: # after this is new line deletion
                            cursorx += 1
                            if cursory > 0:
                                subtract = len(text[cursory])-cursorx
                                print("dist" + str(subtract))
                                print("Combined: " + combinedtext)
                                print("a: " + combinedtext[:cursorx+getxbetween(cursory)])
                                print("b: " + combinedtext[cursorx+1+getxbetween(cursory):] )
                                try:
                                    if text[cursory]:
                                        pass
                                    text = text[:cursory-1] + [text[cursory-0] + text[cursory+1]]
                                except:
                                    print(text[:cursory-1])
                                    print("-1" + text[cursory-1])
                                    print("y" + text[cursory])
                                    print("combination" + text[cursory-1] + text[cursory+0])
                                    text = text[:cursory-1] + [text[cursory-1] + text[cursory+0]] # test1 test2 test3
                                print(text)
                                cursory -= 1
                                cursorx = len(text[cursory])
                                cursorx -= subtract
                    if keytext == "Delete":

                        cursorx += 1
                        if cursorx != len(text[cursory])+1:
                            text[cursory] = text[cursory][:cursorx-1] + text[cursory][cursorx:]
                            cursorx -= 1
                        else: # after this is new line deletion
                            print("Delete key line deletion will be added soon.")


                    if keytext == "":
                        current = text[cursory][cursorx:]
                        text[cursory] = text[cursory][:cursorx]
                        cursorx = 0
                        cursory += 1
                        text.insert(cursory,current)
                    if keytext == chr(9):
                        text[cursory] = text[cursory][:cursorx] + "        " + text[cursory][cursorx+1:]
                print(text)

    pos = (25,25)
    i2 = -1
    combinedtext = '\n'.join(text)
    allowkeydownevt = 1
    del tempmousexloc,tempmouseyloc
    for i in text:
        i2 += 1
        wrappingi = []

        wrappingindex = 0
        while len(wrappingi) >= charsforwrapx:
            wrappingindex += 1
            wrappingi.append(i[81*(wrappingindex-1):81*wrappingindex])
        if wrappingindex == 0:
            wrappingi = [i]

        for wrapi in wrappingi:
            if i2 == cursory:
                time.sleep(0.05)
                displaytext = font.render(wrapi,True,white)
                displaynumber = font.render(str(i2+1),True,lightgray)
                square = font.render("█",True,gray)
                pos = (25,pos[1]+12*1.5)
                sidenumberpos = (0,pos[1])
                for i in range(0,len(text[cursory])):
                    lolx = i
                    loly = cursory
                    print("x, y, ss, se: " + str(lolx) + " " + str(loly) + " " + str(selectstart) + " " + str(selectend))
                    if lolx+getxbetween(loly) in range(selectstart,selectend):
                        display.blit(square,(((lolx-25)*11)+25),((loly-25)*18)+25)

                display.blit(displaytext,pos)
                pos = (pos[0]-5+(11*cursorx),pos[1])
                displaybar = font.render("|",True,white)
                if cursorvis:
                    display.blit(displaybar,pos)
                display.blit(displaynumber,sidenumberpos)
            else:
                wrappingindex = []
                while len(wrappingi) >= charsforwrapx:
                    wrappingindex += 1
                    wrappingi.append(i[:81*wrappingindex])


                for wrapi in wrappingi:
                    displaynumber = font.render(str(i2+1),True,gray)
                    displaytext = font.render(wrapi,True,white)
                    pos = (25,pos[1]+12*1.5)
                    sidenumberpos = (0,pos[1])
                    display.blit(displaytext,pos)
                    display.blit(displaynumber,sidenumberpos)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
