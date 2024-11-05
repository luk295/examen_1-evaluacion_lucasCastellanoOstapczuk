# Práctica 6: Configuración cliente + servidor DNS

### Engade ó docker-compose do DNS outro servicio (container) que faga a función de cliente.

Creo un arquivo docker compose modificando o arquivo un pouco o arquivo anterior:

```
services:
  bind:
    image: internetsystemsconsortium/bind9:9.18
    container_name: bin-dns_Practica_6
    tty: true
    ports:
      - 55:53/udp
      - 55:53/tcp
    #- 127.0.0.1:953:953/tcp
    #volumes:
    #  - ./configuracionOpciones:/etc/bind
    #   - ./conf:/etc/bind
    #  - ./zonas:/var/lib/bind
    networks:
      - dns_subred

      
  cliente:
    image: alpine  
    container_name: alpine-cliente
    tty: true
    
    networks:
      - dns_subred
      
networks:
  dns_subred:
    driver: bridge
```

A primera imaxe é do servidor e a segunda é do cliente dns, que é o alpine

Creé la red `dns_subred`. Máis adelante a a continuación...


### Usa unha imaxe alpine

Feito



### Instala, se é preciso, os paquetes que precises para usar no cliente os comando de rede do seguinte enlace.

Comprobo que ten `ip a` e `ìfconfig` con cada máquina e funciona:
### Servidor DNS bind:
```
:

/ # ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
24: eth0@if25: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue state UP 
    link/ether 02:42:ac:15:00:02 brd ff:ff:ff:ff:ff:ff
    inet 172.21.0.2/16 brd 172.21.255.255 scope global eth0
       valid_lft forever preferred_lft forever
/ # 



/ # ifconfig
eth0      Link encap:Ethernet  HWaddr 02:42:AC:15:00:02  
          inet addr:172.21.0.2  Bcast:172.21.255.255  Mask:255.255.0.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:105 errors:0 dropped:0 overruns:0 frame:0
          TX packets:38 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:14495 (14.1 KiB)  TX bytes:3036 (2.9 KiB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

/ # 



```

### Cliente alpine:

```
/ # ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
26: eth0@if27: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue state UP 
    link/ether 02:42:ac:15:00:03 brd ff:ff:ff:ff:ff:ff
    inet 172.21.0.3/16 brd 172.21.255.255 scope global eth0
       valid_lft forever preferred_lft forever
/ # 


/ # ifconfig
eth0      Link encap:Ethernet  HWaddr 02:42:AC:15:00:03  
          inet addr:172.21.0.3  Bcast:172.21.255.255  Mask:255.255.0.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:82 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:13022 (12.7 KiB)  TX bytes:0 (0.0 B)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

/ # 

```

## Comprobo que os contenedores están efectivamente conectados na rede creada no docker compose
Fago `docker network inspect` nome da rede creada co docker compose:

```
luk@luk-VirtualBox:~/P6.-DNS--Docker-compose/proyecto_compose$ docker network inspect proyecto_compose_dns_subred
[
    {
        "Name": "proyecto_compose_dns_subred",
        "Id": "372141aa685e10492177c2ae156daabeb5ce8a89b726069d56dd7a172bf3034b",
        "Created": "2024-11-05T18:30:48.873146481+01:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.21.0.0/16",
                    "Gateway": "172.21.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "0494c08b13dcfe53a42daf8c7175a1f56e838bf622facf75cb76caeeae31cc55": {
                "Name": "alpine-cliente",
                "EndpointID": "bdfb179cdf77934dba8b701cd2ca1799666c257704cddf450bd7022471a1abde",
                "MacAddress": "02:42:ac:15:00:03",
                "IPv4Address": "172.21.0.3/16",
                "IPv6Address": ""
            },
            "488bd7c3655cc6e8054cd422f4c37b8e8cf131a1bf516f842f49995cd1be2e17": {
                "Name": "bin-dns_Practica_6",
                "EndpointID": "f88765726e84fe312d6a31411c57f628046528ac035a679a0b1dfce4439c64bd",
                "MacAddress": "02:42:ac:15:00:02",
                "IPv4Address": "172.21.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {
            "com.docker.compose.network": "dns_subred",
            "com.docker.compose.project": "proyecto_compose",
            "com.docker.compose.version": "2.29.2"
        }
    }
]
```

### Se pode comprobar que efectivamente as máquinas foron creadas na mesma rede e que coinciden as ips.

### Fai a instalación de dig se é preciso.

### Configura o cliente para que o seu DNS sexa o otro container, modificando el resolv.conf ou usando o fichero docker-compose.yml (preferible)

### Compróbao con 'dig'.

### Resposta: adxunta o repositorio e completa o Readme có realizado (comandos para instalar paquetes y pruebas con 'dig'), explicando a configuración dos arquivos .yml e os seus parámetros

