# LaTeX Makefile
 
PROJECT=formulasheet
OUTPUT=formulasheet

BIBER=biber
PDFLATEX=pdflatex -file-line-error -interaction=nonstopmode -output-directory . -jobname $(OUTPUT) $(PROJECT)
BIBTEX=bibtex
RM = rm -rf

 
UNAME := $(shell uname)
 
# $(call convert_to_png, input.pdf, output,png)
define convert_to_png_lnx
	convert -density 150 $(1) -quality 90 $(2)
endef
define convert_to_png_mac
	sips -s format png --out $(2) $(1)
endef
 
all: $(OUTPUT).pdf
 
$(OUTPUT).pdf : *.tex
	$(PDFLATEX)
	# $(BIBTEX) $(OUTPUT)
	# $(BIBER) $(OUTPUT).bcf
	$(PDFLATEX)
	$(PDFLATEX)

docker: 
	docker run -v `pwd`:/source noah95/latex /usr/bin/make


clean:
	$(RM) *.aux *.bbl *.blg *.log *.out *.pdf
