from setuptools import setup

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mingyu',
    maintainer_email='ache159@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        
        	'vn_longitude = py_pubsub.vn_longitude:main',
        	'vn_latitude = py_pubsub.vn_latitude:main',
        	'vn_pitch = py_pubsub.vn_pitch:main',
        	'vn_roll = py_pubsub.vn_roll:main',
        	'vn_time = py_pubsub.vn_time:main',
        	'vn_yaw = py_pubsub.vn_yaw:main',
        	'vn_vector3 = py_pubsub.vn_vector3:main',
        	'vn_navsatfix = py_pubsub.vn_navsatfix:main',
        	'vn_300 = py_pubsub.vn_300:main',
        	
        	      	
        	'listener = py_pubsub.subscriber_member_function:main',      
        ],
    },
)
