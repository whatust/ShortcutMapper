" Ward off unexpectable
set nocompatible
filetype off

" Set runtimepath to include Vundle

call plug#begin()
Plug 'christoomey/vim-tmux-navigator'   " Vim tmux shotcuts
Plug 'vim-airline/vim-airline'		    " Status tabline
Plug 'vim-airline/vim-airline-themes'	" Status tabline them
Plug 'tpope/vim-fugitive'               " Git commands from within vim
Plug 'benmills/vimux'                   " Open prompt and run tests
Plug 'junegunn/fzf.vim'                 " Fuzzyfinder
Plug 'scrooloose/nerdtree'              " Treed directory navigator
Plug 'Xuyuanp/nerdtree-git-plugin'      " Show git status on NerdTreen
Plug 'vim-perl/vim-perl'                " Syntax highlight for perl language
Plug 'preservim/nerdcommenter'          " Comment block of code
"Plug 'ryanoasis/vim-devicons'           " Add icons to vim
Plug 'Glench/Vim-Jinja2-Syntax'         " Adds syntax hilight for Jinja2
Plug 'vim-python/python-syntax'         " Improves python syntax highlight
Plug 'preservim/nerdcommenter'          " Comment Assistant
Plug 'airblade/vim-gitgutter'           " Adds git diff marks
Plug 'terryma/vim-multiple-cursors'     " Adds multiple cursors
Plug 'vim-pandoc/vim-pandoc-syntax'     " Adds pandoc syntaxhiligth
Plug 'vimwiki/vimwiki'                  " Personal wiki for vim
Plug 'ap/vim-css-color'                 " Adds color preview on source
Plug 'mhartington/oceanic-next'         " Vim Colorscheme
Plug 'rakr/vim-one'                     " Vim Colorscheme
Plug 'arcticicestudio/nord-vim'         " Vim Colorscheme
Plug 'rhysd/git-messenger.vim'          " Git commit message visualizer
Plug 'godlygeek/tabular'                " Tab Alignment
Plug 'neoclide/coc.nvim', {'branch': 'release'}
call plug#end()
filetype plugin indent on

syntax enable

if exists('+termguicolors')
    let &t_8f="\<Esc>[38;2;%lu;%lu%lum"
    let &t_8b="\<Esc>[48;2;%lu;%lu%lum"
    set termguicolors
endif

" Syntax color scheme
colorscheme whatust
"set background=dark

" Tabline theme
let g:airline_theme='deus'

" Use Patched fonts arrows and tirangles
let g:airline_powerline_fonts=1

" Remove character encoding from airline tab
let g:airline#parts#ffenc#skip_expected_string='utf-8[unix]'

" Allow space for alignment and tab for indentations
let g:airline#extensions#whitespace#mixed_indent_algo = 2


" Identation
set autoindent

" Indentation optimions
set tabstop=4
set softtabstop=4
set shiftwidth=4
set noexpandtab

" Change tab for spaces
set expandtab

" Allow backspace over autoident
set backspace=indent,eol,start

" Set max column marker
set colorcolumn=81

" Ask to confirm instead of failing exit command
set confirm

" Show partial commands on the last line of the screen
set showcmd

" Set command line height to 2 characters
set cmdheight=1

" Use utf-8 for character encoding
set encoding=utf-8
set fileencoding=utf-8

" Highlight serach matches
set hlsearch

" Stop redrawing during operations
set lazyredraw

" Display unprintable characters
" set list

" Enable use of mouse on all modes
set mouse=a

" Line number
set number relativenumber

" Wildmenu
set wildmenu

" Prevent some cursor moviment from going to the start of the line
set nostartofline

" Highlight cursor
set cursorline

" Quickly time out on keycodes, remove timout on mappings
set notimeout ttimeout ttimeoutlen=200

" Allows shell alias from vim shell
set shell=bash

" Case sensitive search
set smartcase

" Use already open file on open file command
set switchbuf=useopen

" Use visual bell instead of beaping
set visualbell

" Autoreload files when changed (e.g. git checkout)
set autoread

" Disable visual bell removing beeping and flash
set t_vb=

" Set cursor automatic position
set scrolloff=10

" Paste mode
set pastetoggle=<F3>

" Let fzf work on tmux
let g:fzf_prefer_tmux = 1

" Function to make tmux zoom its runner pane.
function! VimuxZoomRunner()
    call VimuxInspectRunner()
    call system("tmux resize-pane -Z")
endfunction

" Grep shortcut
if executable('ag')
    set grepprg=ag\
    let g:ctrlp_user_command = 'ag %s -l --cocolor -g ""'
endif

" Change line hilight on insert mode
autocmd InsertEnter,InsertLeave * set cul!

set guicursor=n-v-c-sm:block,i-ci-ve:ver20,r-cr-o:hok20

" Changerelative number and global number
augroup numbertoggle
    autocmd!
    autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
    autocmd BufLeave,FocusLost,InsertEnter   * set norelativenumber
augroup END

" Rebalance windows on vim resize
autocmd Vimresized * :wincmd =

" NERDTree
set modifiable
let NERDTreeShowHidden=1

" Gitmessenger Color
"hi gitmessengerPopupNormal term=None guibg=#1b2b34 guifg=#dddddd
"hi gitmessengerHeader      term=None guibg=#1b2b34 guifg=#5fb3b3
"hi gitmessengerHash        term=None guibg=#1b2b34 guifg=#ff7400
"hi gitmessengerHistory     term=None guibg=#1b2b34 guifg=#c594c5

" Vim Wiki
let g:vimwiki_list = [{ 'path': '~/.local/vimwiki/', 
            \ 'template_path': '~/.local/vimwiki/templates/',
            \ 'path_html': '~/.local/vimwiki/site_html',
            \ 'template_default': 'default', 
            \ 'custom_wiki2html': 'vimwiki_markdown',
            \ 'html_filename_parameterization': 1,
            \ 'template_ext': '.tpl', 'syntax': 'markdown', 'ext': '.md'}]

"""""""""""
" Hotkeys "
"""""""""""

" Map leader
let mapleader = ","

" Remove multicursor default keybinds
let g:multi_cursor_use_default_mapping=0

" Multicursor hotkey mapping
" let g:multi_cursor_start_word_key      = '<C-w>'
" let g:multi_cursor_select_all_word_key = '<A-n>'
" let g:multi_cursor_start_key           = 'g<C-n>'
" let g:multi_cursor_select_all_key      = 'g<A-n>'
" let g:multi_cursor_next_key            = '<C-w>'
" let g:multi_cursor_prev_key            = '<C-p>'
" let g:multi_cursor_skip_key            = '<C-x>'
"  let g:multi_cursor_quit_key            = '<Esc>'

" Global

" Mapping fzf search commands
noremap <A-n> :GFiles<CR>
noremap <C-n> :Files<CR>

" Vimux
noremap <C-c> :VimuxPromptCommand<CR>
noremap <C-a> :VimuxRunLastCommand<CR>
noremap <C-i> :VimuxInspectRunner<CR>
" noremap <C-q> :VimuxCloseRunner<CR>
" noremap <C-x> :VimuxInterruptRunner<CR>

" NERDTree control map
map <C-t> :NERDTreeToggle<CR>

" Remove higlight
map <Leader>n :noh<CR>

" Boxes
vmap <F2> !boxes -s 80 -p a1 -a c <CR>
vmap <F3> !boxes -s 80 -dshell -p a1 -a c <CR>
vmap <C-s> :Tabular /

" Normal Mode

" Vertical split
nnoremap <silent> vv <C-w>v

" Remove trailing whitespaces
nmap <F2> :%s/\s\+$//e <CR>

" Open git messenger window
nmap <C-g> :GitMessenger<CR>
nmap <A-g> :GitGutterSignsToggle<CR>

" GoTo code navigation.
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

" Shortcut for git commands
" nmap <Leader>gb :Gblame<CR>
" nmap <Leader>gs :Gstatus<CR>
" nmap <Leader>gd :Gitdiff<CR>
" nmap <Leader>gcm :Gitcommit<CR>
" nmap <Leader>gco :!git checkout

" Get word syntax group
nmap <C-S-p> :call <SID>SynStack()<CR>
function! <SID>SynStack()
    if !exists("*synstack")
        return
    endif
    echo map(synstack(line('.'), col('.')), 'synIDattr(v:val, "name")')
endfunc

" Insert Mode

" Escape using kj
imap kj <Esc>
imap Kj <Esc>
imap kJ <Esc>
imap KJ <Esc>

" coc Completion
inoremap <silent><expr> <TAB> pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<C-TAB>" :
      \ coc#refresh()

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

