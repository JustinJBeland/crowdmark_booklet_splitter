gs -o all_booklets_flattened.pdf -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress \
  -dNOPAUSE -dBATCH -dSAFER -dDetectDuplicateImages=true \
  -dCompressFonts=true -dEmbedAllFonts=true -dFlattenPageForms=true \
  -f all_bookelts.pdf
