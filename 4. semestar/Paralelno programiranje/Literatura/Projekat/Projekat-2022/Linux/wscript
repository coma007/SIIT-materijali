#!/usr/bin/env python3
# encoding: utf-8

'''
@author: Milos Subotic <milos.subotic.sm@gmail.com>
@license: MIT

'''

###############################################################################

import os
import sys
import fnmatch
import shutil
import datetime
import glob

import waflib

###############################################################################

APPNAME = 'PP_Project'

top = '.'

###############################################################################

def prerequisites(ctx):
	pass

def options(opt):
	opt.load('gcc gxx')
	
	opt.add_option(
		'--app',
		dest = 'app',
		default = None,
		help = 'App to be run'
	)
	
def configure(cfg):
	cfg.load('gcc gxx')
	
	cfg.env.append_value('CXXFLAGS', '-std=c++11')
	#cfg.env.append_value('LIB', 'pthread')
	cfg.env.append_value('CXXFLAGS', '-g -rdynamic'.split()) # For debug.

	cfg.check_cfg(
		package = 'tbb',
		uselib_store = 'tbb',
		args = '--cflags --libs',
		mandatory = True
	)


def build(bld):
	
	bld.program(
		features = 'cxx',
		use = 'tbb',
		rpath = bld.env['LIBPATH_tbb'],
		target = 'ImageProcessing',
		source = [
			'main.cpp',
			'BitmapRawConverter.cpp',
			'EasyBMP.cpp',
		]
	)
	







def run(ctx):
	'''./waf run --app=<NAME>'''
	if ctx.options.app:
		if sys.platform == 'win32':
			# MSYS2
			ctx.exec_command2('build\\' + ctx.options.app)
		else:
			ctx.exec_command2('./build/' + ctx.options.app)

###############################################################################

def exec_command2(self, cmd, **kw):
	# Log output while running command.
	kw['stdout'] = None
	kw['stderr'] = None
	ret = self.exec_command(cmd, **kw)
	if ret != 0:
		self.fatal('Command "{}" returned {}'.format(cmd, ret))
setattr(waflib.Context.Context, 'exec_command2', exec_command2)

###############################################################################

def recursive_glob(pattern, directory = '.'):
	for root, dirs, files in os.walk(directory, followlinks = True):
		for f in files:
			if fnmatch.fnmatch(f, pattern):
				yield os.path.join(root, f)
		for d in dirs:
			if fnmatch.fnmatch(d + '/', pattern):
				yield os.path.join(root, d)

def collect_git_ignored_files():
	for gitignore in recursive_glob('.gitignore'):
		with open(gitignore) as f:
			base = os.path.dirname(gitignore)
			
			for pattern in f.readlines():
				pattern = pattern[:-1]
				for f in recursive_glob(pattern, base):
					yield f

###############################################################################

def distclean(ctx):
	for fn in collect_git_ignored_files():
		if os.path.isdir(fn):
			shutil.rmtree(fn)
		else:
			os.remove(fn)

def dist(ctx):
	now = datetime.datetime.now()
	time_stamp = '{:d}-{:02d}-{:02d}-{:02d}-{:02d}-{:02d}'.format(
		now.year,
		now.month,
		now.day,
		now.hour,
		now.minute,
		now.second
	)
	ctx.arch_name = '../{}-{}.zip'.format(APPNAME, time_stamp)
	ctx.algo = 'zip'
	ctx.base_name = APPNAME
	# Also pack git.
	waflib.Node.exclude_regs = waflib.Node.exclude_regs.replace(
'''
**/.git
**/.git/**
**/.gitignore''', '')
	# Ignore waf's stuff.
	waflib.Node.exclude_regs += '\n**/.waf*'
	
###############################################################################
