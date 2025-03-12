# Intranet Django

Bem-vindo(a) ao projeto de **Intranet** desenvolvido em **Django**! Este README fornece instruções para construir e executar a aplicação usando **Docker** e **Docker Compose**, além de alguns passos básicos de configuração.

---

## Índice
1. [Visão Geral](#visão-geral)  
2. [Pré-Requisitos](#pré-requisitos)  
3. [Como Usar](#como-usar)  
   - [1. Clonar o Repositório](#1-clonar-o-repositório)  
   - [2. Build da Imagem Docker](#2-build-da-imagem-docker)  
   - [3. Subir o Contêiner](#3-subir-o-contêiner)  
   - [4. Criar Superusuário](#4-criar-superusuário)  
4. [Acessando a Aplicação](#acessando-a-aplicação)  
5. [Comandos Úteis](#comandos-úteis)  
6. [Contribuição](#contribuição)  
7. [Licença](#licença)  

---

## Visão Geral
Este projeto é uma aplicação **Intranet** desenvolvida com o framework **Django**. O objetivo é fornecer um ambiente interno para a organização, com funcionalidades de autenticação, administração, etc. Usamos contêineres Docker para simplificar o processo de configuração e execução, garantindo um ambiente consistente em diferentes máquinas.

---

## Pré-Requisitos
- **Git**: para clonar o repositório (opcional, caso prefira baixar o código de outra forma).
- **Docker** e **Docker Compose**: para construir e executar a aplicação em contêineres.

Verifique se ambos estão instalados e atualizados:
```bash
docker --version
docker compose version
