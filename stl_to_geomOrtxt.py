#!/usr/bin/python
import struct
import sys

# this program reads binary format file and converts to Vertex file for sogang university's graphics file format
# save normalized vector and vertex 1, 2, 3 which makes triangles to the data class
# this program is console program. If you want to execute it , input #python3 stl.py example.stl
# stl file formatd은 삼각형에 대한것이라서, 법선벡터가 1개밖에 없지만, 원래는 각꼭지점마다 다 있으므로 
#법선벡터는 세개 있어야 한다. 따라서 설사 같은것이라도 세번 파일 롸잇 해야할듯.
# 이 프로그램은 바이너리 포맷 파일을 읽어들이고 ( *.stl) 이 것을 각 꼭지점들을 실수로 바꾸어주는 프로그램이다.
# 혹은 stl 파일 포맷을 읽고 이것을 서강대 그래픽스 숙제 파일 형시에 맞는 geom 파일로 변환시킨다. 그러나 tex 없는 6개 짜리임. 
class binary_data:
    def __init__(self):
        self.normalVector = b'abc'
        self.Vertex1 = b'abc'
        self.Vertex2 = b'a'
        self.Vertex3 = b'c'

class data:
    normalVector=()
    Vertex1=()
    Vertex2=()
    Vertex3=()
    def __init__(self):
        pass

def file_read():
    fname = sys.argv[1]

    f=open(fname,'rb') #binary file read
    flag = input("choose the file type, t is text file format, and b is binary file format: ")
    if(flag == "t"):
     
        f.read(80) #ignore 80 byte

        #read the number of triangles
        s=f.read(4)
        numberOfTriangle = struct.unpack("<L",s)[0]

        dataSet = []
        for i in range(0, numberOfTriangle):
            dataSet.append(data())

        for i in range(0, numberOfTriangle):
            # read normalized vector, 한국말로 법선벡터
            s=f.read(4)
            nx=struct.unpack("<f",s)[0] # convert binary format to IEEE floating point

            s=f.read(4)
            ny=struct.unpack("<f",s)[0]

            s=f.read(4)
            nz= struct.unpack("<f",s)[0]

            dataSet[i].normalVector = (nx,ny,nz)# save normalized Vector

            #read Vertex1
            s=f.read(4)
            x=struct.unpack("<f",s)[0]
            s=f.read(4)
            y=struct.unpack("<f",s)[0]
            s=f.read(4)
            z=struct.unpack("<f",s)[0]

            dataSet[i].Vertex1 = (x,y,z) # save Vertex1

            #read Vertex2
            s=f.read(4)
            x=struct.unpack("<f",s)[0]
            s=f.read(4)
            y=struct.unpack("<f",s)[0]
            s=f.read(4)
            z=struct.unpack("<f",s)[0]
            dataSet[i].Vertex2 = (x,y,z) # save Vertex2

            #read Vertex3
            s=f.read(4)
            x=struct.unpack("<f",s)[0]
            s=f.read(4)
            y=struct.unpack("<f",s)[0]
            s=f.read(4)
            z=struct.unpack("<f",s)[0]
            dataSet[i].Vertex3 = (x,y,z) #save Vertex3

            f.read(2) #ignore 2 byte
        f.close()
    
    elif(flag =="b"):
            f.read(80) # ignore 80bytes
            s=f.read(4)
            numberOfTriangle_byte = s
            numberOfTriangle = struct.unpack("<L",s)[0]
            dataSet = []
            for i in range(0, numberOfTriangle):
                dataSet.append(binary_data())
            for i in range(0,numberOfTriangle):
                #read normalized Vector 
                s=f.read(12) # 4 bytes per vertex
                dataSet[i].normalVector=s
                
                # read Vertex1
                s=f.read(12)
                dataSet[i].Vertex1 = s

                #read Vertex2
                s = f.read(12)
                dataSet[i].Vertex2 = s
                
                #read Vertex3
                s=f.read(12)
                dataSet[i].Vertex3 = s
                
                #ignore 2 byte
                f.read(2)
    

    if(flag == "t"):
        
        return (numberOfTriangle,dataSet) # return the vertex array set
    
    elif(flag =="b"):
        return (numberOfTriangle_byte,dataSet)

def file_write (numberOfTriangle, dataSet ): # file write function
    fileName= input("Input file name to write: ")

    newline="\r\n" # because of windows system 
    flag = input("choose file format txt or geom: ")
    if(flag == "txt"):
        fileName +=  ".txt"
        flag = "t"
    else:
        fileName =fileName+ ".geom"
        flag = "g"
    if(flag =="t"):
        
        f=open(fileName,'w')
        f.write(str(numberOfTriangle))
        f.write(newline)
        for i in range(0, numberOfTriangle):
            data= "%f %f %f" %(dataSet[i].Vertex1[0], dataSet[i].Vertex1[1],dataSet[i].Vertex1[2])
            f.write(data)
            f.write(newline)
            data= "%f %f %f" %(dataSet[i].Vertex2[0], dataSet[i].Vertex2[1],dataSet[i].Vertex2[2])
            f.write(data)
            f.write(newline)
            data= "%f %f %f" %(dataSet[i].Vertex3[0], dataSet[i].Vertex3[1],dataSet[i].Vertex3[2])
            f.write(data)
            f.write(newline)

        f.close()
    
    elif(flag == "g"):

        f=open(fileName,'wb')
        f.write((numberOfTriangle))
        for i in dataSet:
            f.write(i.Vertex1)
            f.write(i.normalVector)
            f.write(i.Vertex2)
            f.write(i.normalVector)
            f.write(i.Vertex3)
            f.write(i.normalVector)

    return

def main():
    (numberOfTriangle, dataSet) = file_read()
    file_write(numberOfTriangle,dataSet)
    return

if __name__ == "__main__":
         main()





