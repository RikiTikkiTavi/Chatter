WITH words as (
  SELECT synset_id
  FROM term
  WHERE word = '{}'
)
SELECT DISTINCT term.synset_id
FROM term
       RIGHT JOIN words ON words.synset_id = term.synset_id
;
