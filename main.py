import subprocess
import pdflatex as PDFLaTeX

path = 'G:/FIles/test1/400000.jpg'


string=''
for i in range (60):
    string+=(r'''
\multirow{3}{*}{\includegraphics[width=0.1\textwidth]{%s}}&  \roundedcellname{\small{11126 228}} & 
\multirow{2}{*}{\includegraphics[width=0.1\textwidth]{%s}} & \roundedcellname{\small{11127 229}} &
\multirow{2}{*}{\includegraphics[width=0.1\textwidth]{%s}} & \roundedcellname{\small{11127 230}} &
\multirow{2}{*}{\includegraphics[width=0.1\textwidth]{%s}} & \roundedcellname{\small{11127 231}}
\\ 

& \tiny{Very good product for your purchase} & 
& \tiny{Superb product} &
& \tiny{Excellent product} &
& \tiny{Medium product for out dear clients} \\[+0.6cm]
& \roundedcellprice{\tiny{EUR 90}} \roundedcellprice{\tiny{EUR 80}} & 
& \roundedcellprice{\tiny{EUR 30}} \roundedcellprice{\tiny{EUR 25}} & 
& \roundedcellprice{\tiny{EUR 20}} \roundedcellprice{\tiny{EUR 15}} & 
& \roundedcellprice{\tiny{EUR 10}} \roundedcellprice{\tiny{EUR 5}} \\
\midrule
''')% (path, path, path, path)
content = (r'''
\documentclass[9pt]{article}
\usepackage{graphicx}
\usepackage[bottom=0.7in,top=0.1in, left=0in]{geometry}
\usepackage{lmodern}
\usepackage{iftex}
\usepackage{textcomp} % provide euro and other symbols
\usepackage{multirow,makecell}


\usepackage{xcolor}
\usepackage{longtable}
\usepackage{calc} % for calculating minipage widths
\usepackage{tabularx}
\usepackage{ booktabs}
\usepackage{lipsum}
\usepackage{tikz}

\usepackage[framemethod=TikZ]{mdframed}

\author{
John Smith\\University XYZ\\Albert Square\\Walford\\NC1 8AE
}
\begin{document}

New manual

\newpage



\addtolength{\tabcolsep}{-4.2pt}
\newcommand\roundedcellname[1]{
    \begin{tikzpicture}
        \filldraw[fill=gray!130, rounded corners=3mm] (0,0) rectangle (3.0cm,0.5cm);
        \node[text=white] at (1.5cm, 0.25cm) {#1};
    \end{tikzpicture}
}

\newcommand\roundedcellprice[1]{
    \begin{tikzpicture}
        \filldraw[fill=gray!15, rounded corners=3mm] (0,0) rectangle (1.4cm,0.6cm);
        \node[text=black] at (0.7cm, 0.3cm) {#1};
    \end{tikzpicture}
}

\newcommand\roundedcellthird[1]{
    \begin{tikzpicture}
        \filldraw[fill=gray!20, rounded corners=0mm] (0,0) rectangle (2cm,0.6cm);
        \node[text=black] at (1.0cm, 0.3cm) {#1};
    \end{tikzpicture}
}

\begin{longtable}{cp{3.3cm}cp{3.3cm}cp{3.3cm}cp{3.3cm}} ''') + string+ (r'''




\end{longtable}


\label{fig:nature}
  

\end{document}''')
#            + (r'''
# \noindent\includegraphics[width=3cm]{%s}\vspace*{-10cm} \colorbox{red}{"title"} \includegraphics[width=3cm]{%s} \large "title"
#
# ''')% (path, path) + r'''
# \textbf{\huge  \\}
# \vspace{1cm}
# \textbf{\Large  \\}
#
# \end{document}
# ''')


with open('cover.tex','w') as f:
    f.write(content)#%args.__dict__)

file='cover.tex'
subprocess.call(['pdflatex', 'cover.tex'])
