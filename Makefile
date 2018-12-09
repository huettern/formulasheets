
all:
	cd template && make && cd ..
	cd Leistungselektronik && make && cd ..

docker:
	cd template && make docker && cd ..
	cd Leistungselektronik && make docker && cd ..

clean:
	cd template && make clean && cd ..
	cd Leistungselektronik && make clean && cd ..
