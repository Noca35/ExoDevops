<h1 align="center">ExoDevops</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1-blue.svg?cacheSeconds=2592000" />
</p>

Exercice Devops dont le but est d'écrire un operateur kubernetes minimaliste

> L'objectif de l'opérateur est de definir une Custom Ressource Mall qui correspond à un centre commercial qui contient N boutiques et l'item vendu par ces boutiques
> Grâce à ces données, l'operateur va dimensionner le nombre de pod qui correspond aux N boutiques et definir l'item vendu basé sur les valeurs de la custom ressource.
> Les informations sur le nom de la boutique ainsi que l'objet vendu seront affiché chaques secondes dans les différents pod de la boutique. 

## Installation de l'environnement

> Près requis :
>	* Hyperviseur
>	* Kubectl
>	* Minikube
>	* Framework python kopf	

guide d'installation :

https://kubernetes.io/fr/docs/tasks/tools/install-minikube/


## Test du déploiement

```sh
minikube start
minikube dashboard
```

A ce stade le dashboard kubernetes devrait apparaitre à l'écran

## Usage

1.Dans notre cas l'opérateur va être déployé dans le cluster, on va devoir donc lui attribuer les droits nécéssaire à son bon fonctionnement

```sh
kubectl apply -f crd.yaml ## definition de la custom ressource
kubectl apply -f role-operator.yaml ## definition des rôles de l'operateur
kubectl apply -f rol_bind-operator.yaml ## application des rôles à l'operateur 
```
2.Deploiement de l'operateur dans le cluster

```sh
kubectl apply -f operator-deployment.yaml
```

3.Definition des ressources de la galerie marchande

```sh
kubectl apply -f mall.yaml
```

4.Confirmation de la création des ressources

A ce stade une configmap "mall-config" a du être créée avec l'item "socks" ainsi que 10 pods shop basé sur la custom ressource mall.yaml :

```yaml
apiVersion: mall.my.domain/v1
kind: Mall
metadata:
  name: mall-first
spec:
  replicas: 10
  item: socks
```

replicas correspondant au nombre de boutique dans la gallerie marchande et item l'objet vendu

5.Affichage du message d'information

Commençons par lister les pods déployés

```sh
kubectl get pods --all-namespaces
```

Et ensuite affichons les logs d'un pod shop au choix en remplaçant my-pod par un des pods shop listé

```sh
kubectl logs -f my-pod
```

Le message retournant le nom du shop ainsi que l'objet vendu devrait apparaître

6.scalabilité des shop

Modifions la ressource malls.yaml :

```yaml
apiVersion: mall.my.domain/v1
kind: Mall
metadata:
  name: mall-first
spec:
  replicas: 5
  item: socks
```

Appliquons la :

```sh
kubectl apply -f mall.yaml
```

Verifions le nombre de pods déployés:

```sh
minikube dashboard
```
Le nombre de pods shop devrait déscendre à 5


7.Test de suppression de la ressource mall.yaml

```sh
kubectl delete -f mall.yaml
```

Avec cette commande on observe que les pods shop on été supprimé ainsi que la configmap "mall-config"


## Author

👤 **Noca35**

