# Práctica 6: Configuración cliente + servidor DNS

### Engade ó docker-compose do DNS outro servicio (container) que faga a función de cliente.
>[!NOTA]
>ACTUALIZO EL DOCKER COMPOSE PARA PODER ASIGNAR EL DNS AL CLIENTE. MODIFICO DIRECCIÓN IP E NETWORK. E ENGADO NO MESMO ARQUIVO TODA A CONFIGURACIÓN, ONDE ESPECIFICO A DIRECCIÓN DO DNS

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
    #   - ./conf:/etc/bind/
    #  - ./zonas:/var/lib/bind/
    
    networks:
      lucas:
        ipv4_address: 172.28.1.1
      
  cliente:
    image: alpine  
    container_name: alpine-cliente
    tty: true
    
    dns:
      - 172.28.1.1
    networks:
      lucas:
        ipv4_address: 172.28.1.99
       #caracteristicas de red. rango etc
networks:
  lucas:
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 172.28.0.0/16
          ip_range: 172.28.1.0/24
          gateway: 172.28.1.254

```

A primera imaxe é do servidor e a segunda é do cliente dns, que é o alpine

Creé la red `dns_subred`. Máis detalle a continuación...


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
29: eth0@if30: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue state UP 
    link/ether 02:42:ac:1c:01:63 brd ff:ff:ff:ff:ff:ff
    inet 172.28.1.99/16 brd 172.28.255.255 scope global eth0
       valid_lft forever preferred_lft forever



/ # ifconfig
eth0      Link encap:Ethernet  HWaddr 02:42:AC:1C:01:63  
          inet addr:172.28.1.99  Bcast:172.28.255.255  Mask:255.255.0.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:72 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:11434 (11.1 KiB)  TX bytes:0 (0.0 B)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

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

### Agora probo se vense entre elas co comando `ping`.

cliente a servidor:
```
/ # ping 172.21.0.2
PING 172.21.0.2 (172.21.0.2): 56 data bytes
64 bytes from 172.21.0.2: seq=0 ttl=64 time=0.284 ms
64 bytes from 172.21.0.2: seq=1 ttl=64 time=0.138 ms
64 bytes from 172.21.0.2: seq=2 ttl=64 time=0.124 ms
^C
--- 172.21.0.2 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.124/0.182/0.284 ms
/ # ping 172.21.0.4
PING 172.21.0.4 (172.21.0.4): 56 data bytes
^C
--- 172.21.0.4 ping statistics ---
3 packets transmitted, 0 packets received, 100% packet loss
```


servidor a cliente:

```
/ # ping 172.21.0.3
PING 172.21.0.3 (172.21.0.3): 56 data bytes
64 bytes from 172.21.0.3: seq=0 ttl=64 time=0.129 ms
64 bytes from 172.21.0.3: seq=1 ttl=64 time=0.177 ms
64 bytes from 172.21.0.3: seq=2 ttl=64 time=0.136 ms
64 bytes from 172.21.0.3: seq=3 ttl=64 time=0.154 ms
^C
--- 172.21.0.3 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.129/0.149/0.177 ms
/ # ^C
```
### Fai a instalación de dig se é preciso.

Fixen  `apk update && apk add bind-tools` no cliente alpine.

No bin (servidor) non tiven que agregar nin instalar nada.



### Configura o cliente para que o seu DNS sexa o otro container, modificando el resolv.conf ou usando o fichero docker-compose.yml (preferible)

>[!NOTA]
>ACTUALIZO EL DOCKER COMPOSE PARA PODER ASIGNAR EL DNS AL CLIENTE. MODIFICO DIRECCIÓN IP E NETWORK.

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
    volumes:
    #  - ./configuracionOpciones:/etc/bind
       - ./confi:/etc/bind/          # onde estaraá o arquivo named.conf
       - ./zonas:/var/lib/bind/
    
    networks:
      dns_subred:
        ipv4_address: 172.28.1.1
      
  cliente:
    image: alpine  
    container_name: alpine-cliente
    tty: true
    
    dns:
      - 172.28.1.1
    networks:
      dns_subred:
        ipv4_address: 172.28.1.99
       #caracteristicas de red. rango etc
networks:
  dns_subred:
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 172.28.0.0/16
          ip_range: 172.28.1.0/24
          gateway: 172.28.5.254

```

```
Engado dous carpetas: "confi" e "zonas".

No confi engado o arquivo de configuración:


zone "asircastelao.org" {
	type master;
	file "/var/lib/bind/db.asircastelao.org";
	allow-query {
		any;
		};
	};
	
options {
	directory "/var/cache/bind";

	forwarders {
	 	8.8.8.8;
		1.1.1.1;
	 };
	 forward only;

	listen-on { any; };
	listen-on-v6 { any; };

	allow-query {
		any;
	};
};


NA CARPETA 'zonas' CREO O ARQUIVO da zona:

$TTL 38400	; 10 hours 40 minutes
@		IN SOA	ns.asircastelao.org. some.email.address. (
				10000002   ; serial
				10800      ; refresh (3 hours)
				3600       ; retry (1 hour)
				604800     ; expire (1 week)
				38400      ; minimum (10 hours 40 minutes)
				)
@		IN NS	ns.asircastelao.org.
ns		IN A		172.28.1.1
test	IN A		172.28.1.4
www		IN A		172.28.1.7
alias	IN CNAME	test
texto	IN TXT		PROBA DO DNS




```
### Compróbao con 'dig'.

Co comando dig vou probando se responde:

`dig @172.28.1.1 ns.asircastelao.org`
```
/ # dig @172.28.1.1 ns.asircastelao.org

; <<>> DiG 9.18.27 <<>> @172.28.1.1 ns.asircastelao.org
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 10043
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: fe88dbf22e71271a01000000672e5826ed66a50d46e97cb5 (good)
;; QUESTION SECTION:
;ns.asircastelao.org.           IN      A

;; ANSWER SECTION:
ns.asircastelao.org.    38400   IN      A       172.28.1.1

;; Query time: 0 msec
;; SERVER: 172.28.1.1#53(172.28.1.1) (UDP)
;; WHEN: Fri Nov 08 18:27:50 UTC 2024
;; MSG SIZE  rcvd: 92

```
`dig @172.28.1.1 test.asircastelao.org`
```
/ # dig @172.28.1.1 test.asircastelao.org

; <<>> DiG 9.18.27 <<>> @172.28.1.1 test.asircastelao.org
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 40212
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: ac3613cfa74a807301000000672e58b8ef9b285be2aef4e6 (good)
;; QUESTION SECTION:
;test.asircastelao.org.         IN      A

;; ANSWER SECTION:
test.asircastelao.org.  38400   IN      A       172.28.1.4

;; Query time: 0 msec
;; SERVER: 172.28.1.1#53(172.28.1.1) (UDP)
;; WHEN: Fri Nov 08 18:30:16 UTC 2024
;; MSG SIZE  rcvd: 94

```

`dig @172.28.1.1 www.asircastelao.org`
```

/ # dig @172.28.1.1 www.asircastelao.org

; <<>> DiG 9.18.27 <<>> @172.28.1.1 www.asircastelao.org
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 17824
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: 792dd8dbf731bd8501000000672e590005c228c17a6eb61b (good)
;; QUESTION SECTION:
;www.asircastelao.org.          IN      A

;; ANSWER SECTION:
www.asircastelao.org.   38400   IN      A       172.28.1.7

;; Query time: 0 msec
;; SERVER: 172.28.1.1#53(172.28.1.1) (UDP)
;; WHEN: Fri Nov 08 18:31:28 UTC 2024
;; MSG SIZE  rcvd: 93
```


### Resposta: adxunta o repositorio e completa o Readme có realizado (comandos para instalar paquetes y pruebas con 'dig'), explicando a configuración dos arquivos .yml e os seus parámetros

