;; cosas que les pueden servir en su archivo de configuración emacs

(require 'font-lock)
(require 'shell)
(require 'python-mode)
(progn
  (setq display-time-day-and-date t
        display-time-24hr-format t)
  (display-time))
(prefer-coding-system 'utf-8)
(setq default-buffer-file-coding-system 'utf-8)
(server-start)  ; export EDITOR=emacsserver
(fset 'yes-or-no-p 'y-or-n-p)   ; Always y ws n instead of yes ws no
(require 'ido)
(ido-mode t)
(add-hook 'python-mode-hook 'flycheck-mode)

(global-set-key "\C-cgf" 'find-file-at-point-with-line)

(defun find-file-at-point-with-line()
  "if file has an attached line num goto that line, ie boom.rb:12"
  (interactive)
  (setq line-num 0)
  (save-excursion
    (search-forward-regexp "[^ ]:" (point-max) t)
    (if (looking-at "[0-9]+")
         (setq line-num (string-to-number (buffer-substring (match-beginning 0) (match-end 0))))))
  (find-file-at-point)x
  (if (not (equal line-num 0))
      (goto-line line-num)))

