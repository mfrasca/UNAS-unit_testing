unit testing with python
!!!!!!!!!!!!!!!!!!!!!!!!

día 1
=========

emacs
---------
* que es emacs?

  * editor de texto
  *   primer software libre
  *   ambiente de programación lisp
  *   el programa donde puedes hacerlo todo
  *   hasta el café (htcpcp)
  *   https://es.wikipedia.org/wiki/Emacs

* refcard

  * las refcards no son sólo para emacs, todas son buenas,
  * https://www.gnu.org/software/emacs/refcards/
  
* emacs en windows

  * http://vgoulet.act.ulaval.ca/en/emacs/windows/0
  
* tutoriales

  * http://lostsalad.co.za/2012/05/23/vim-to-emacs
  * http://www.jesshamrick.com/2012/09/10/absolute-beginners-guide-to-emacs/
  
* los primeros días

  * steep learning curve!
  * si eres usuario 'vi': http://www.emacswiki.org/emacs/Evil
  * y sino, utilizandolo, y leyendo los tutoriales y el sistema de help.

python
----------
* porqué python

  * por haber sido desarrollado por matemáticos?
  * por parecerse a pseudo-codigo?
  * por el sistema de paquetes?
  
* caracteristicas de python

  * cfr wikipedia, python.org, y entender los chistes como 'import antigravity'
  
* cómo python

  * utilizandolo!
  * http://diveintopython.org/

trabajar en equipo
------------------------
* software de manejo versiones

  * dos personas, un archivo: caos.
  * una persona, dos programas: igual caos.
  * CVS, subversion, git - solución de conflictos
  
* servicios de versiones

  * sourceforge, bitbucket, launchpad, github
  
* git como idioma, github como jerga

  * el mismo git permite varios flujos de trabajo
  * github sugiere uno, no te obliga
  * en bauble utilizo... master, bauble-1.0, tag, 
  
* el problema de las librerías

  * windows (DLL), cada programa instala las suyas o remplaza las de sistema
    (con cuales resultados)

  * linux, cada programa es distribuido como parte del todo (limitaciones?
    cada distribución tiene sus paquetes, un software puede ser no
    instalable en una versión de linux, la práctica del backporting, )

  * pip+virtualenv de python parecen pensados por programadores sin
    paciencia (un solo método para distribuir en Debian, Mac, Redhat,
    Windows)

día 2
=================

Hello World in PyGTK/glade
-------------------------------

* https://wiki.gnome.org/Projects/PyGTK/QuickStart
* editar en glade

* algo relacionado:

  * http://www.ibm.com/developerworks/java/tutorials/j-jython1/j-jython1.html
  * http://zetcode.com/gui/jythonswing/introduction/

tarea práctica imprescindible
---------------------------------
* preliminar

  * get a github account - now

* crear un módulo

  * yo he creado un repositorio para esta tarea, ustedes hagan:
  * fork
  * clone
  * se trata de un módulo que implementará una sola función
  * la función está descrita en forma textual, traducirlo en pruebas unitarias
  * luego escriben el código que realiza las pruebas
  * para ejecutar las pruebas, correr el módulo
    
* virtualenv

  * crear un entorno virtual (en ~/.virtualenvs)
  * activarlo (. .virtualenvs/<nombre>)
  * install --upgrade pip
  * cual versión de pip tenemos?
  * desactivarlo (deactivate)
  * cual versión de pip tenemos?
  * activar otra vez el entorno virtual
  * instalar nosetests (en el virtualenv, con pip)
  * ejecutar las pruebas con nosetests

día 3
=================
un error común ayer
------------------------
* trabajar como root

  * ¡NO LO HAGAN!
  * trabajando como root, los archivos creados o modificados pertenecen a root.
  * no vas a tener derecho de modificarlos como usuario.
  
* sudo su

  * mejor `sudo lo-que-sea-pero-no-su`
  * `sudo su` los deja como root y puede ser que uno no se acuerde ser root y siga trabajando como root.
  * `sudo su - <username>` esto sí es útil y no es peligroso.
  * siempre miren quien eres: whoami
  * y si el prompt termina en $ ó #
  
* solucionar problemas haciendose root

  * si el elaborador no permite algo, no siempre se soluciona haciendose root.
  * si unix no le permite algo, hay una razón.
  * a root todo le está permitido, hasta `rm -fr /`

* terminar la tarea práctica imprescindible

  * ayer hicimos
  
    * instalamos git y python-virtualenv
    * tomamos una cuenta github
    * miramos https://github.com/mfrasca/UNAS-unit_testing
    
      * de esto cada uno tiene:
      
        * fork - su propio repositorio en github
        * clone - la copia del repositorio en el elaborador

día 4
==================
recapitulación
------------------
* que vimos hasta ahora

  * emacs, python, git, virtualenv, pip, unittest, python modules, nose, 

* vimos y no vimos

  * emacs (en serio), PyGTK, glade, Jython, swing, Bauble, github, 

* preguntas abiertas

  * por favor pregunten

  * existen modulos de pruebas unitarias para postgresql?
  * cual es la estructura de la base de datos bauble

* Presentación del Software Bauble

  * software libre - GPL
  * para colecciones botánicas - (http://www.bgci.org/resources/Living_collections/)
  * conceptos mínimos de taxonomía (Categorias_taxonomicas_es.svg)

* theory: tests first. practice: so sorry

  * http://bauble.readthedocs.org/en/latest/devdl.html#adding-missing-unit-tests
  
* Internacionalización del Software

  * internationalization - i18n
  * localization - l10n

  * bauble/scripts/i18n.sh

  * xgettext, gettext, pygettext, msgmerge
  * https://launchpad.net/bauble
  * https://hosted.weblate.org/projects/bauble/
  * sphinx-intl

* sistemas de apoyo a las pruebas unitarias

  * https://travis-ci.org/Bauble/bauble.classic/
  * https://csvjdbc.ci.cloudbees.com/job/csvjdbc/
  * https://coveralls.io/github/Bauble/bauble.classic

