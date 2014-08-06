CC = g++ -D_REENTRANT -g -O2
CFLAGS =-c -fPIC

OBJS = LandauStandalone.o
SRC =  LandauStandalone.C




all : $(OBJS)  
	$(CC)  $(OBJS)  -o LandauStandalone

LandauStandalone.o : LandauStandalone.C
	$(CC) $(CFLAGS)  LandauStandalone.C  -o LandauStandalone.o


clean : 
	rm *.o LandauStandalone
