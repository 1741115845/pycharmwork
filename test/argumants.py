class Arguments():
    def argumwnt(self,*args,**kwargs):
        print(args)
        print(kwargs)

arguments=Arguments()
arguments.argumwnt([1,1,2],{"a":"ces"},a=3,y=4)