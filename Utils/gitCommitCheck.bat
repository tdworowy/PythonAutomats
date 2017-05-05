if [ -n "$(git status --porcelain)" ]; then
   git commit -m "Commit from jenkins"
 else
  echo "no changes";
fi
