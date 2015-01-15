from __future__ import print_function
from docker import Client

DATA_CONTAINER = 'data'
BACKUP_ROOT = '/home/eecheverry/Backups/Docker/'

cli = Client(base_url='unix://var/run/docker.sock')

containers = cli.containers()
volumes_dict = {}

try:
    volumes_dict = cli.inspect_container(DATA_CONTAINER)['Volumes']
except Exception as e:
    print("ERROR:", e)

volumes = [volume for volume in volumes_dict]
print(volumes)

for i, volume in enumerate(volumes):
    container = cli.create_container(image='tebanep/odoo-base', volumes=['/backup'],
                                     command='tar cvf /backup/backup.tar ' + volume,
                                     detach=True)

    container_id = container['Id']
    container_backup_directory = BACKUP_ROOT + DATA_CONTAINER + volume
    print(container_backup_directory)
    cli.start(container_id, volumes_from=DATA_CONTAINER, binds={
        container_backup_directory: {
            'bind': '/backup',
            'ro': False
        }
    })

    cli.remove_container(container_id, force=True)
