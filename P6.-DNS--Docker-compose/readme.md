# Práctica 6: Configuración cliente + servidor DNS

CARACTERISTICAS DE LA RED:

[
    {
        "Name": "bridge",
        "Id": "68a70d38a558318722fd7d2ea0df16332bb7632acb28d6926c20cb6a32b28646",
        "Created": "2024-11-04T17:16:25.551538783+01:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
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
        "Containers": {},
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]


docker network inspect proyecto_compose_dns_subred
[
    {
        "Name": "proyecto_compose_dns_subred",
        "Id": "8a3faf45793a0b5057defdddb5a577e4daf300d0690a78974770f91113f59c74",
        "Created": "2024-11-04T18:36:36.070062268+01:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.22.0.0/16",
                    "Gateway": "172.22.0.1"
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
            "3c22a13f614306fa28bbb0ffc15311f689ec06eb2274912d009da1554139772a": {
                "Name": "alpine-cliente",
                "EndpointID": "368ae170d69bfa1854df8cd00b9064eef0385f53accbeac25a354330bd0be41d",
                "MacAddress": "02:42:ac:16:00:02",
                "IPv4Address": "172.22.0.2/16",
                "IPv6Address": ""
            },
            "5e0ce403c6695b5022307d19a1a02919cb2eae2b78c5379ca28165e3585189e2": {
                "Name": "bin-dns_Practica_6",
                "EndpointID": "17b5ff3c62842cb56f9ad985a96174973fd2607d57c3a5e078315263d93e3bb1",
                "MacAddress": "02:42:ac:16:00:03",
                "IPv4Address": "172.22.0.3/16",
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

Creé la red `dns_subred`. 
As características da rede son de bridge. Polo que máis adelante tendré que inspeccionar las direcciones para configurar la dirección dns y se vean


### Usa unha imaxe alpine


### Instala, se é preciso, os paquetes que precises para usar no cliente os comando de rede do seguinte enlace.






### Comproba o seu uso

### Fai a instalación de dig se é preciso.

### Configura o cliente para que o seu DNS sexa o otro container, modificando el resolv.conf ou usando o fichero docker-compose.yml (preferible)

### Compróbao con 'dig'.

### Resposta: adxunta o repositorio e completa o Readme có realizado (comandos para instalar paquetes y pruebas con 'dig'), explicando a configuración dos arquivos .yml e os seus parámetros

