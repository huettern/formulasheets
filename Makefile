
all:
	cd template && make && cd ..
	cd Leistungselektronik && make && cd ..
	cd Analysis\ III\ \-\ PDE && make && cd ..

docker:
	cd template && make docker && cd ..
	cd Leistungselektronik && make docker && cd ..
	cd Analysis\ III\ \-\ PDE && make docker && cd ..

clean:
	cd template && make clean && cd ..
	cd Leistungselektronik && make clean && cd ..
	cd Analysis\ III\ \-\ PDE && make clean && cd ..
