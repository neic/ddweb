((python . ((eval . (setq python-shell-virtualenv-path (concat
                                                     (locate-dominating-file
                                                      buffer-file-name ".dir-locals.el")
                                                     "venv"
                                                     ))))))
