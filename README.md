# DeepLearning_Trading_Full_Data

# 📊 AI Portfolio Arena

Une plateforme collaborative de simulation boursière basée sur l'IA.  
Les utilisateurs peuvent soumettre des stratégies d’investissement (via IA/ML), suivre leurs performances, se comparer à d'autres et s’abonner aux meilleurs portefeuilles.

---

## 🚀 Objectif du projet

Créer un **MVP** (Produit Minimum Viable) d'une application web :
- Permettant aux utilisateurs de **soumettre des modèles IA** prédictifs ou des portefeuilles simulés.
- Calculant la **performance en temps réel** (ROI, Sharpe Ratio, drawdown...).
- Affichant un **classement public** basé sur les performances.
- Offrant un système de **suivi / abonnement** à des portefeuilles prometteurs.

---

## 🧱 Stack technique

| Côté        | Tech utilisée                  |
|-------------|-------------------------------|
| Frontend    | Next.js, Tailwind CSS         |
| Backend     | FastAPI, Pydantic             |
| Base de données | PostgreSQL + TimescaleDB |
| Auth        | JWT (JSON Web Tokens)         |
| ML          | Python (scikit-learn, PyTorch, Prophet...) |
| Conteneurisation | Docker, Docker Compose   |
| Déploiement | Vercel (frontend), Render (backend + DB) |

---

## 📦 Fonctionnalités principales

- ✅ Authentification (register/login)
- ✅ Upload de portefeuille ou stratégie IA
- ✅ Simulation boursière (données historiques)
- ✅ Calculs financiers (ROI, Sharpe, drawdown)
- ✅ Leaderboard public
- ✅ Suivi / abonnement aux portefeuilles
- 🚧 Notifications (plus tard)
- 🚧 Intégration données live (plus tard)

---

## 🖼️ Aperçu (mockup/demo)

> (À ajouter quand tu auras une interface !)

---

## 🔧 Installation locale

### 1. Cloner le projet

```bash
git clone https://github.com/ton-utilisateur/ai-portfolio-arena.git
cd ai-portfolio-arena