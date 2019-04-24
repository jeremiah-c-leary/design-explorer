import design_explorer as de

def create (self):

    oReturn = de.hw.fpga.create('max10m50')

    oReturn.datasheet = 'https://www.intel.com/content/dam/www/programmable/us/en/pdfs/literature/hb/max-10/m10_overview.pdf'
    return oReturn

