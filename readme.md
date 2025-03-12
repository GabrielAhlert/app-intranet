
# 🖥️ App Intranet

Este projeto é uma aplicação web desenvolvida em Django, pronta para ser implantada com Docker, proporcionando uma solução robusta e eficiente para gerenciar sua intranet corporativa.

> **Nota:** Este projeto está atualmente configurado com o layout específico da empresa onde trabalho. Para utilizar em outro ambiente, será necessário personalizar o layout conforme suas necessidades.

> **Nota:** Esta configuração Docker é destinada apenas para uso em ambiente de desenvolvimento.

---

## ⚙️ Funcionalidades

- Gestão simplificada de conteúdo interno
- Autenticação segura de usuários
- Administração intuitiva com Django Admin
- Auto-reload durante o desenvolvimento (salvou, atualizou)

---

## 🛠️ Requisitos

Certifique-se de ter os seguintes softwares instalados:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 🚀 Como executar

Clone este repositório e acesse o diretório:

```bash
git clone https://github.com/GabrielAhlert/app-intranet.git
cd app-intranet
```

Em seguida, construa e execute o projeto com os seguintes comandos:

```bash
docker build -t django-docker .
docker compose up -d
```

Crie um usuário administrador para acessar o painel Django Admin:

```bash
docker-compose exec django-web python manage.py createsuperuser
```

Acesse a aplicação no navegador através de:

```
http://localhost:8000
```

Para acessar o painel administrativo Django, utilize:

```
http://localhost:8000/admin
```

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte [LICENSE](LICENSE) para detalhes.

---

✨ **Desenvolvido com Django e Docker** ✨
