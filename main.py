#!/usr/bin/python\
import reg as reg
import mem as mem
import function as function
import J_type as jtype
import I_type as itype
import toFile as toFile

instruction="start jalr   2   4" # test J type
opcode = ""
filePath = "file/testAllFunction.txt"
toFile.read(filePath)

# --------------- Beginnig I type ---------
#machineLanguage = itype.iType(machineLanguage)
#print ("machineLanguage [ I type ] : " + machineLanguage)
#print ("machineLanguage [ J type ] :  : "+ jtype.J_type(instruction))