from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.VuRemote'
setup(name='enigma2-plugin-systemplugins-remotecontrolcode',
       version='3.0',
       description='Change Remote Control Code',
       package_dir={pkg: 'VuRemote'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
