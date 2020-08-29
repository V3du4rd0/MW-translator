import maya.cmds
import math
import subprocess
import ast

def truncate(number, digits) :
    stepper = pow(10.0, digits)
    return math.trunc(stepper * number) / stepper


objname=maya.cmds.ls(sl=1)[0]
dicV={}
for i in range(maya.cmds.polyEvaluate(objname,v=1)):
    x,y,z=maya.cmds.pointPosition(objname+'.vtx['+str(i)+']')
    dicV[i+1]=(truncate(x,3),truncate(y,3),truncate(z,3)) 

Lf=[]
str_faces=''
for i in range(maya.cmds.polyEvaluate(objname,f=1)):
	maya.cmds.select(objname+'.f['+str(i)+']')
	maya.cmds.select(maya.cmds.polyListComponentConversion(ff=1,tv=1))
	Lf.append(maya.cmds.ls(sl=1))
for fs in Lf:
	cara=[]
	if len(fs)==3:
		for elem in fs:
			v=str(elem)
			i=v.find('[')
			j=v.find(']')
			cara.append(eval(v[i+1:j]))
	elif len(fs)==1:
		v=str(fs[0])
		i=v.find('[')
		j=v.find(']')
		k=v.find(':')
		cara=[elem for elem in range(eval(v[i+1:k]),eval(v[k+1:j])+1)]
	elif len(fs)==2:
		for elem in fs:
			v=str(elem)
			i=v.find('[')
			j=v.find(']')
			if ':' in v:
				k=v.find(':')
				cara.append(eval(v[i+1:k]))
				cara.append(eval(v[k+1:j]))
				
			else:
				cara.append(eval(v[i+1:j]))
			
	else:
		print 'no 3 face'
	str_faces+='{'+str(cara[0]+1)+','+str(cara[1]+1)+','+str(cara[2]+1)+'},'
		

print str_faces
str_faces='{Polygon[{'+str_faces[:-1]+'}]}'


str_vtx=''
L2=dicV.keys()
L2.sort()
for v in L2:
	a,b,c=dicV[v]
	str_vtx+='{'+str(a)+','+str(b)+','+str(c)+'},'
str_vtx=str_vtx[:-1]
str_vtx='{'+str_vtx+'}'

st='MeshRegion['+str_vtx+','+str_faces+']'
print st
func='''  
#Erase this line and write your code here
'''

# You may need to modify the line 77
# if your "func" function is not the Wollfram's Douglas Plateau problem solver
# or your model doesn't hold the algorithm hypothesis
st=func+'SS='+st+'; SS2=areaGradientDescent[SS, 1., 20., False]; Print[MeshCoordinates[SS2]]'
print st
out = subprocess.Popen(["wolframscript" ,"-code", st], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

salida = out.communicate()[0]
i=salida.find('{')
j=salida.rfind('}')
print salida[:i]
t=salida[i+1:j].replace('{','(')
t=t.replace('}',')')
L=list(ast.literal_eval(t))

for i in range(len(L)):
	maya.cmds.move(L[i][0],L[i][1],L[i][2],objname+'.vtx['+str(i)+']')
print 'done'
maya.cmds.select(objname)
#		
